from rest_framework.generics import ListAPIView, RetrieveAPIView
from store.models import Order
from .serializers import OrderSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer