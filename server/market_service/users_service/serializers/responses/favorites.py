from users_service.serializers.models import FavoritesInternalListSerializer
from users_service.serializers.responses.base import (
    PaginatedResponseSerializer
)

from rest_framework.pagination import DjangoPaginator


class FavoritesPaginatedResponseSerializer(PaginatedResponseSerializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        super().__init__(paginator, page_number)
        self._data["results"] = FavoritesInternalListSerializer(
            instance=self.page.object_list,
            many=True
        ).data
