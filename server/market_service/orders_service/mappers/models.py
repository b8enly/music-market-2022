from orders_service.models import PayMethod, DeliveryMethod, Order, ProductSet
from django.db.models import QuerySet
from uuid import UUID


class PayMethodMapper:
    @staticmethod
    def get() -> QuerySet[PayMethod]:
        return PayMethod.objects.all()


class DeliveryMethodMapper:
    @staticmethod
    def get() -> QuerySet[DeliveryMethod]:
        return DeliveryMethod.objects.all()


class OrdersMapper:
    @staticmethod
    def get_order_by_number(number: int) -> Order:
        return Order.objects.get(number=number)

    @staticmethod
    def get_orders_by_user_id(user_id: UUID) -> QuerySet[Order]:
        return Order.objects.filter(user_id=user_id)


class ProductSetMapper:
    @staticmethod
    def get_product_set_by_id(set_id: UUID) -> QuerySet[ProductSet]:
        return ProductSet.objects.filter(product_set_id=set_id)
