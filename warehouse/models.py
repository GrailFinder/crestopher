from django.db import models
from django.db.models.signals import post_save
import uuid


class Order(models.Model):
    id = models.CharField(max_length=128, null=False, unique=True, primary_key=True, default=uuid.uuid1)
    amount = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.id}: {self.created_at}'

    class Meta:
        app_label = 'warehouse'

