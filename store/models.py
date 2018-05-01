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


from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@broker"
}

def sync_sign(sender, instance, created, *args, **kwargs):
    # make rpc call
    print(sender, instance, created)
    with ClusterRpcProxy(config) as cluster_rpc:
        order_dict = instance.__dict__
        order_dict.pop('_state')
        order_dict['created_at'] = order_dict['created_at'].timestamp()
        order_dict['updated_at'] = order_dict['updated_at'].timestamp()
        print('order dict:', order_dict)
        cluster_rpc.sync.sync_order(order_dict, created)

post_save.connect(sync_sign, sender=Order)