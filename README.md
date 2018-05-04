# Crestopher
## Two way sync between two apps

Backend rest api service that contains two applications: Store & Warehouse. Each of the app has its own database and Order model/table. After store_order being created service creates (through [Celery](http://docs.celeryproject.org/en/latest/)) warehouse_order. If warehouse_order updates its status store_order also would be updated.

![how it is pic](closet/scheme1.png "scheme1")


## Routes to call (store_orders)
```
urlpatterns = [
    path('orders/', OrderListView.as_view()),
    re_path(r'^orders/(?P<pk>[0-9a-f-]+)/$', OrderRetrieveView.as_view()),
    re_path(r'^orders/(?P<pk>[0-9a-f-]+)/update/$', OrderUpdateView.as_view()),
]
```

## How to run it
The best way is to use docker-compose because there is too many dependencies you need to get otherwise.

1. First of all get containers running
```
docker-compose up -d --build
```
2. Make it run migrations (order matters)
```
docker-compose run crestopher python manage.py makemigrations warehouse
docker-compose run crestopher python manage.py migrate --database=warehouse

docker-compose run crestopher python manage.py makemigrations store
docker-compose run crestopher python manage.py migrate --database=store
```
3. To have access to admin panel you need to create admin (here username would be admin and password: hard2crack)
```
docker-compose run crestopher python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'hard2crack')"
```
4. Now you can create store_order, go to the http://0.0.0.0:8000/admin/store/order/add/  
**dont change default status though, theres check in code for "some status" that decides if update is needed for store_order**

5. Check logs or view db gui for newly created warehouse_orders
```
docker-compose logs crestopher
```
store_db
```
docker exec -ti store_db psql -U postgres -W
Password for user postgres: postgres
select * from store_order;
```
warehouse_db
```
docker exec -ti warehouse_db psql -U postgres -W
Password for user postgres: postgres
select * from warehouse_order;
```
