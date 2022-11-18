from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.pagination import DjangoPaginator

from products_service.serializers.responses.products_response import ProductSerializer
from products_service.serializers.responses.brand_response import BrandSerializer
from products_service.serializers.responses.category_response import CategorySerializer
from products_service.serializers.responses.type_response import TypeResponse
from products_service.mappers.models.category_mapper import CategoryMapper
from products_service.mappers.models.type_mapper import TypeMapper
from products_service.mappers.models.brand_mapper import BrandMapper
from products_service.serializers.responses.brand_response import BrandSerializer

from uuid import UUID


class ProductsPaginatedResponse(Serializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int
    ):
        self.paginator = paginator
        self.page = paginator.get_page(page_number)
    
    @property
    def data(self):
        return {
            "count": self.paginator.count,
            "next": (
                None if not self.page.has_next()
                else self.page.next_page_number()
            ),
            "previous": (
                None if not self.page.has_previous()
                else self.page.previous_page_number()
            ),
            "page_size": self.paginator.per_page,
            "results": ProductSerializer(instance=self.page.object_list, many=True).data
        }
