from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from store.models import Order
from .serializers import OrderSerializer, OrderUpdateSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer