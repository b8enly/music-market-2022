from products_service.exceptions.service.exceptions import ValidationException
from products_service.exceptions.service.exceptions import NotFoundException
from products_service.mappers.models.category_mapper import CategoryMapper
from products_service.mappers.models.type_mapper import TypeMapper
from products_service.mappers.models.product_mapper import ProductMapper

from rest_framework.serializers import Serializer, CharField, UUIDField
from typing import Any
from uuid import UUID


class CategoryProductsRequest(Serializer):
    page_size = CharField(required=True)
    category_id = UUIDField(required=True)

    def validate_paginator_parameter(self, value: Any, parameter: str) -> int:
        if value is None:
            raise ValidationException(
                detail=f"{parameter} parameter is required"
            )
        if isinstance(value, str) and not value.isdigit():
            raise ValidationException(
                detail=f"{parameter} parameter must be integer"
            )
        value = int(value)
        if value < 1:
            raise ValidationException(
                detail=f"{parameter} parameter must be equal or greater than 1"
            )
        return value

    def validate_category_id(self, id: UUID) -> UUID:
        if not isinstance(id, UUID):
            raise ValidationException(f"{id} - must be valid uuid string")
        if not CategoryMapper.get_category_by_id(id=id):
            raise NotFoundException(f"category with id {id} not found")
        return id
        

    def validate(self, attrs: dict):
        self.page = self.validate_paginator_parameter(
            value=attrs.get("page"),
            parameter="page"
        )
        self.page_size = self.validate_paginator_parameter(
            value=attrs.get("page_size"),
            parameter="page_size"
        )
        self.category_id = self.validate_category_id(
            id=attrs.get("category_id")
        )
        return self


class CategoryTypeProductsRequest(CategoryProductsRequest):
    type_id = UUIDField(required=True)

    def validate_type_id(self, id: UUID) -> UUID:
        if not isinstance(id, UUID):
            raise ValidationException(f"{id} - must be valid uuid string")
        if not TypeMapper.get_by_id(id=id):
            raise NotFoundException(f"type with id {id} not found")
        return id
    
    def validate(self, attrs: dict):
        self.type_id = self.validate_type_id(id=attrs.get("type_id"))
        return super().validate(attrs)


class ProductDetailRequest(Serializer):
    product_id = UUIDField()

    def validate_product_id(self, id: UUID) -> UUID:
        if not isinstance(id, UUID):
            raise ValidationException(f"{id} - must be valid uuid string")
        if not ProductMapper.get_by_id(id=id):
            raise NotFoundException(f"product with id {id} not found")
        return id
    
    def validate(self, attrs: dict):
        self.product_id = self.validate_product_id(id=attrs.get("product_id"))
        return self
