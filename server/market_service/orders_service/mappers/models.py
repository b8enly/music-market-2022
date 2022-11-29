from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from uuid import UUID

from orders_service.models import PayMethod, DeliveryMethod, ProductSet, Order
from uuid import UUID, uuid4


class PayMethodMapper:
    @staticmethod
    def get() -> QuerySet[PayMethod]:
        return PayMethod.objects.all()

    @staticmethod
    def get_by_id(id: UUID) -> PayMethod:
        try:
            return PayMethod.objects.get(id=id)
        except ObjectDoesNotExist:
            return None


class DeliveryMethodMapper:
    @staticmethod
    def get() -> QuerySet[DeliveryMethod]:
        return DeliveryMethod.objects.all()
    
    @staticmethod
    def get_by_id(id: UUID) -> DeliveryMethod:
        try:
            return DeliveryMethod.objects.get(id=id)
        except ObjectDoesNotExist:
            return None


class OrdersMapper:
    @staticmethod
    def get_order_by_number(number: int) -> Order:
        return Order.objects.get(number=number)

    @staticmethod
    def get_orders_by_user_id(user_id: UUID) -> QuerySet[Order]:
        return Order.objects.filter(user_id=user_id)


class ProductSetMapper:
    @staticmethod
    def get_by_id(id: UUID) -> DeliveryMethod:
        try:
            return DeliveryMethod.objects.get(id=id)
        except ObjectDoesNotExist:
            return None


class ProductSetMapper:
    @staticmethod
    def create(user_id: UUID, product_ids: list[UUID]) -> UUID:
        product_set_id = uuid4()
        
        products = list(map(
            lambda product_id: ProductSet(
                product_set_id=product_set_id,
                user_id=user_id,
                product_id=product_id
            ),
            product_ids
        ))

        ProductSet.objects.bulk_create(products)

        return product_set_id

    @staticmethod
    def get_product_set_by_id(set_id: UUID) -> QuerySet[ProductSet]:
        return ProductSet.objects.filter(product_set_id=set_id)


class OrderMapper:
    @staticmethod
    def create(
        user_id: UUID,
        product_set_id: UUID,
        payment_method_id: PayMethod,
        delivery_method_id: DeliveryMethod
    ) -> Order:
        order = Order(
            user_id=user_id,
            product_set=product_set_id,
            payment_method=payment_method_id,
            delivery_method=delivery_method_id
        )
        order.save()

        return order
