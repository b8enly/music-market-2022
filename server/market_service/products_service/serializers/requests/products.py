from products_service.serializers.requests.base import (
    PaginatedRequestSerializer
)
from products_service.exceptions.service import (
    ValidationException, 
    NotFoundException
)
from products_service.mappers.models import (
    CategoryMapper, 
    ProductMapper, 
    BrandMapper,
    TypeMapper
)

from rest_framework.serializers import UUIDField, Serializer
from uuid import UUID


def validate_type_id(id: UUID) -> UUID:
    if not TypeMapper.get_by_id(id=id):
        raise NotFoundException(f"type with id {id} not found")
    return id


class CategoryProductsRequestSerializer(PaginatedRequestSerializer):
    category_id = UUIDField(required=True)

    def validate_category_id(self, id: UUID) -> UUID:
        if not CategoryMapper.get_by_id(id=id):
            raise NotFoundException(f"category with id {id} not found")
        return id
        

    def validate(self, attrs: dict):
        self.category_id = self.validate_category_id(
            id=attrs.get("category_id")
        )
        return super().validate(attrs=attrs)


class BrandProductsRequestSerializer(PaginatedRequestSerializer):
    brand_id = UUIDField(required=True)

    def validate_brand_id(self, id: UUID) -> UUID:
        if not BrandMapper.get_by_id(id=id):
            raise NotFoundException(f"brand with id {id} not found")
        return id
        

    def validate(self, attrs: dict):
        self.brand_id = self.validate_brand_id(
            id=attrs.get("brand_id")
        )
        return super().validate(attrs=attrs)


class CategoryTypeProductsRequestSerializer(CategoryProductsRequestSerializer):
    type_id = UUIDField(required=True)
    
    def validate(self, attrs: dict):
        self.type_id = validate_type_id(id=attrs.get("type_id"))
        return super().validate(attrs)


class BrandTypeProductsRequestSerializer(BrandProductsRequestSerializer):
    type_id = UUIDField(required=True)

    def validate(self, attrs: dict):
        self.type_id = validate_type_id(id=attrs.get("type_id"))
        return super().validate(attrs)


class ProductDetailRequest(Serializer):
    product_id = UUIDField()

    def validate_product_id(self, id: UUID) -> UUID:
        if not ProductMapper.get_by_id(id=id):
            raise NotFoundException(f"product with id {id} not found")
        return id
    
    def validate(self, attrs: dict):
        self.product_id = self.validate_product_id(id=attrs.get("product_id"))
        return self
