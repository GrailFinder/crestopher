# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from urllib import request as req
from datetime import datetime
import time
import json
from random import random

@shared_task
def sync_order(order):
    from warehouse.models import Order
    existing_order = Order.objects.filter(id=order['id'])
    if not existing_order or existing_order.updated_at < order['updated_at']:  # if None or newer
        resp = req.urlopen(f"http://0.0.0.0:8000/store/orders/{order['id']}").read().decode("utf-8")
        resp = json.loads(resp)

        #if random() > .1:  # 90% status would be updated
        print("status was updated")
        resp['status'] = "updated status"

        new_order = Order(id=resp['id'], amount=resp['amount'], price=resp['price'],
                    comment=resp['comment'], created_at=convert_time(resp['created_at']),
                    updated_at=convert_time(resp['updated_at']),
                    status=resp['status'])
        new_order.save()
        
def convert_time(dts):
    try:
        dt = datetime.strptime(dts, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        dt = datetime.strptime(dts, "%Y-%m-%dT%H:%M:%SZ")
    return dt