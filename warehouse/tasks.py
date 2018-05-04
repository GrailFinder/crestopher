# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from urllib import request as req
from datetime import datetime
import time
from warehouse.models import Order
import json

@shared_task
def sync_order(order):
    print(order)
    time.sleep(2)    

    existing_order = Order.objects.filter(id=order['id'])
    if not existing_order or existing_order.updated_at < order['updated_at']:  # if None or newer
        resp = req.urlopen(f"http://0.0.0.0:8000/store/orders/{order['id']}").read().decode("utf-8")
        print("got response:", resp)
        print("rsp type:", type(resp))
        print(len(resp))
        resp = json.loads(resp)
        new_order = Order(id=resp['id'], amount=resp['amount'], price=resp['price'],
                    comment=resp['comment'], created_at=datetime.strptime(resp['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    updated_at=datetime.strptime(resp['updated_at'], "%Y-%m-%dT%H:%M:%S.%fZ"))
        new_order.save()
        