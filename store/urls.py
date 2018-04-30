
from django.urls import path
from store.api.views import OrderListView

urlpatterns = [
    path('orders/', OrderListView.as_view()),
]
