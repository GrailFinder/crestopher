from nameko.rpc import rpc
from urllib import request as req
import time

class OrderSyncService:
    name = 'sync'

    @rpc
    def sync_order(self, order, created):
        if created:
            # add to db
            print(order)
            time.sleep(10)
        else:
            # make http request to get data?
            resp = req.urlopen("0.0.0.0:8000/store/orders/").read().decode("utf-8")
            print(resp)
