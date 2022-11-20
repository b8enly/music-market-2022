from users_service.models import Cart
from django.db.models import QuerySet
from uuid import UUID


class CartMapper:
    @staticmethod
    def create(user_id: str, product_id: str) -> None:
        Cart(user_id=UUID(user_id), product_id=UUID(product_id)).save()

    @staticmethod
    def get_cart_products_by_user_id(user_id: str) -> QuerySet[Cart]:
        return Cart.objects.filter(user_id=UUID(user_id))

    @staticmethod
    def delete(user_id: str, product_id: str) -> None:
        Cart.objects.filter(user_id=UUID(user_id), product_id=UUID(product_id)).delete()