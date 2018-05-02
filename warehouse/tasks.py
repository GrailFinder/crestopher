# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from urllib import request as req
from datetime import datetime
import time
from warehouse.models import Order

@shared_task
def sync_order(order):
    print(order)
    time.sleep(2)
    resp = req.urlopen(f"http://0.0.0.0:8000/store/orders/{order['id']}").read().decode("utf-8")
    print("got response:", resp)

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