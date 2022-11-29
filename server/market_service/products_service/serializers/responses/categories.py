from products_service.serializers.models import CategorySerializer
from products_service.serializers.responses.base import (
    PaginatedResponseSerializer
)

from rest_framework.pagination import DjangoPaginator


class CategoriesLimitResponseSerializer(CategorySerializer):
    pass


class CategoriesPaginatedResponseSerializer(PaginatedResponseSerializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        super().__init__(paginator, page_number)
        self._data["results"] = CategorySerializer(
            instance=self.page.object_list,
            many=True
        ).data        
