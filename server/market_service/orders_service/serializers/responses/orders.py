from orders_service.serializers.models import OrderSerializer
from orders_service.serializers.responses.base import (
    PaginatedResponseSerializer
)
from orders_service.models import Order

from rest_framework.pagination import DjangoPaginator


class OrderDetailResponseSerializer(PaginatedResponseSerializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int,
        order: Order
    ):
        super().__init__(paginator, page_number)
        self._data["order"] = OrderSerializer(
            instance=[order], 
            many=True
        ).data[0]
