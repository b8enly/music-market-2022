from products_service.exceptions.service.exceptions import ValidationException
from products_service.exceptions.service.exceptions import NotFoundException
from products_service.mappers.models.brand_mapper import BrandMapper
from products_service.mappers.models.type_mapper import TypeMapper

from rest_framework.serializers import Serializer, CharField, UUIDField
from typing import Any
from uuid import UUID


class BrandProductsRequest(Serializer):
    page_size = CharField(required=True)
    brand_id = UUIDField(required=True)

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

    def validate_brand_id(self, id: UUID) -> UUID:
        if not isinstance(id, UUID):
            raise ValidationException(f"{id} - must be valid uuid string")
        if not BrandMapper.get_brand_by_id(id):
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
        self.brand_id = self.validate_brand_id(
            id=attrs.get("brand_id")
        )
        return self


class BrandTypeProductsRequest(BrandProductsRequest):
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
