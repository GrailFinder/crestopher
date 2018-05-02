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


# from nameko.standalone.rpc import ClusterRpcProxy

# config = {
#     'AMQP_URI': "pyamqp://guest:guest@broker"
# }

# def sync_sign(sender, instance, created, *args, **kwargs):
#     # make rpc call
#     print(sender, instance, created)
#     with ClusterRpcProxy(config) as cluster_rpc:
#         order_dict = instance.__dict__
#         order_dict.pop('_state')
#         order_dict['created_at'] = order_dict['created_at'].timestamp()
#         order_dict['updated_at'] = order_dict['updated_at'].timestamp()
#         print('order dict:', order_dict)
#         cluster_rpc.sync.sync_order(order_dict, created)

# post_save.connect(sync_sign, sender=Order)



# from nameko.rpc import rpc
# from urllib import request as req
# from datetime import datetime
# import time
# class OrderSyncService:
#     name = 'sync'
#     @rpc
#     def sync_order(self, order, created):
#         if created:
#             # add to db
#             print(order)
#             time.sleep(10)
#             print('done waiting')
#             has_it = Order.objects.filter(id=order['id'])
#             if not has_it:
#                 new_order = Order(id=order['id'], amount=order['amount'], price=order['price'],
#                 comment=order['comment'], created_at=datetime.fromtimestamp(order['created_at']),
#                 updated_at=datetime.fromtimestamp(order['updated_at']))
#                 new_order.save()
#         else:
#             # make http request to get data?
#             resp = req.urlopen(f"0.0.0.0:8000/store/orders/{order['id']}").read().decode("utf-8")
#             print(resp)
