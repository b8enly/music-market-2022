from products_service.serializers.models import BrandSerializer
from products_service.serializers.responses.base import (
    PaginatedResponseSerializer
)

from rest_framework.pagination import DjangoPaginator


class BrandLimitResponseSerializer(BrandSerializer):
    pass


class BrandPaginatedResponseSerializer(PaginatedResponseSerializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        super().__init__(paginator, page_number)
        self._data["results"] = BrandSerializer(
            instance=self.page.object_list,
            many=True
        ).data
