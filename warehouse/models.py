from django.db import models
from django.db.models.signals import post_save
import uuid
from django.utils import timezone
from store.tasks import update_order_status

class Order(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    amount = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(null=False, default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)   
    status = models.CharField(max_length=128, default="some status")


    def __str__(self):
        return f'{self.id}: {self.status}'

    class Meta:
        app_label = 'warehouse'

def sync_sign(sender, instance, created, *args, **kwargs):
    # make rpc call
    print(sender, instance, created)
    if instance.status != "some status":     # if its not default status
        di = {"id": instance.id, "status": instance.status}
        update_order_status.delay(di)

post_save.connect(sync_sign, sender=Order)