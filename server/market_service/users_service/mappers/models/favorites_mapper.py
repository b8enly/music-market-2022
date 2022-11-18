from users_service.models import Favorites

from django.db.models import QuerySet

from uuid import UUID


class FavoritesMapper:
    @staticmethod
    def create(user_id: str, product_id: str) -> None:
        Favorites(user_id=UUID(user_id), product_id=UUID(product_id)).save()

    @staticmethod
    def get_favorites_by_user_id(user_id: str) -> QuerySet[Favorites]:
        return Favorites.objects.filter(user_id=UUID(user_id))

    @staticmethod
    def delete(user_id: str, product_id: str) -> None:
        Favorites.objects.filter(user_id=UUID(user_id), product_id=UUID(product_id)).delete()
