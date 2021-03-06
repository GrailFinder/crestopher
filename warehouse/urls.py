
from django.urls import path, re_path
from store.api.views import OrderListView, OrderRetrieveView, OrderUpdateView

urlpatterns = [
    path('orders/', OrderListView.as_view()),
    re_path(r'^orders/(?P<pk>[0-9a-f-]+)/$', OrderRetrieveView.as_view()),
    re_path(r'^orders/(?P<pk>[0-9a-f-]+)/update/$', OrderUpdateView.as_view()),
]
