from products_service.serializers.requests.base import (
    PaginatedRequestSerializer,
    LimitRequestSerializer,
)


class BrandsLimitRequestSerializer(LimitRequestSerializer):
    pass


class BrandsPaginatedRequestSerializer(PaginatedRequestSerializer):
    pass
