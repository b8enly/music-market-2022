from users_service.models import Favorites, Cart, User
from users_service.exceptions.mappers import (
    UserMapperUpdateException,
    MapperCreateException,
)

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.db.models import QuerySet

from uuid import UUID


class FavoritesMapper:
    @staticmethod
    def create(user_id: UUID, product_id: UUID) -> None:
        try:
            Favorites(user_id=user_id, product_id=product_id).save()
        except IntegrityError as e:
            raise MapperCreateException(e.args)

    @staticmethod
    def get_by_user_id_and_product_id(
        user_id: UUID, 
        product_id: UUID
    ) -> Favorites:
        try: 
            return Favorites.objects.get(user_id=user_id, product_id=product_id)
        except ObjectDoesNotExist:
            return None
    
    @staticmethod
    def find_by_user_id(user_id: UUID) -> QuerySet[Favorites]:
        return Favorites.objects.filter(user_id=user_id)

    @staticmethod
    def delete(user_id: UUID, product_id: UUID) -> None:
        FavoritesMapper.get_by_user_id_and_product_id(
            user_id=user_id,
            product_id=product_id
        ).delete()


class UsersMapper:
    @staticmethod
    def get_by_id(user_id: UUID) -> User:
        try:
            User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        return User.objects.get(id=UUID(user_id))

    @staticmethod
    def get_user_by_uuid(id: UUID) -> User:
        return User.objects.get(id=id)

    @staticmethod
    def update_user_by_id(id: str, **update_fields: dict) -> int:
        try:
            return User.objects.filter(id=UUID(id)).update(**update_fields)
        except (ObjectDoesNotExist, ValueError) as e:
            raise UserMapperUpdateException(e.args)


class CartMapper:
    @staticmethod
    def create(user_id: UUID, product_id: UUID) -> None:
        try:
            Cart(user_id=user_id, product_id=product_id).save()
        except IntegrityError as e:
            raise MapperCreateException(e.args)

    @staticmethod
    def get_by_user_id_and_product_id(
        user_id: UUID, 
        product_id: UUID
    ) -> Cart:
        try: 
            return Cart.objects.get(user_id=user_id, product_id=product_id)
        except ObjectDoesNotExist:
            return None
    
    @staticmethod
    def find_by_user_id(user_id: UUID) -> QuerySet[Cart]:
        return Cart.objects.filter(user_id=user_id)

    @staticmethod
    def delete(user_id: UUID, product_id: UUID) -> None:
        CartMapper.get_by_user_id_and_product_id(
            user_id=user_id,
            product_id=product_id
        ).delete()
