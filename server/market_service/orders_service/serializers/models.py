from rest_framework.serializers import ModelSerializer
from orders_service.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
