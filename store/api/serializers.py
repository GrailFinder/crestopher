from rest_framework.serializers import ModelSerializer
from store.models import Order

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'amount',
            'price',
            'comment',
            'created_at',
        ]