from rest_framework.serializers import ModelSerializer
from users_service.models import Favorites
from uuid import UUID


class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"


class FavoritesInternalListSerializer(FavoriteSerializer):
    def to_representation(self, instance: Favorites) -> UUID:
        return instance.product_id
