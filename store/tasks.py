# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import time, json
from store.api.serializers import OrderUpdateSerializer

@shared_task
def update_order_status(status_dict):
    print("got status for update:", status_dict)
    from store.models import Order
    existing_order = Order.objects.filter(id=status_dict['id']).first()
    if existing_order:
        existing_order.status = status_dict['status']
        jorder = dict()
        jorder['price'] = existing_order.price
        jorder['amount'] = existing_order.amount
        jorder['comment'] = existing_order.comment
        jorder['status'] = existing_order.status
        headers = {"content-type": "application/json"}
        url = f"http://0.0.0.0:8000/store/orders/{status_dict['id']}/update/"
        resp = requests.put(url, data=json.dumps(jorder), headers=headers)
        print(resp.status_code, resp.content)