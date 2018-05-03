from django.db import models
from django.db.models.signals import post_save
import uuid
from warehouse.tasks import sync_order

class Order(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    amount = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=128, default="some status")


    def __str__(self):
        return f'{self.id}: {self.created_at}'

    class Meta:
        app_label = 'store'


def sync_sign(sender, instance, created, *args, **kwargs):
    # make rpc call
    print(sender, instance, created)
    di = {"id": instance.id, "updated_at": instance.updated_at}
    sync_order.delay(di)

post_save.connect(sync_sign, sender=Order)
