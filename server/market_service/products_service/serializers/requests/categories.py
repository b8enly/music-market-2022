from products_service.serializers.requests.base import (
    PaginatedRequestSerializer,
    LimitRequestSerializer,
)


class CategoriesLimitRequestSerializer(LimitRequestSerializer):
    pass


class CategoriesPaginatedRequestSerializer(PaginatedRequestSerializer):
    pass
