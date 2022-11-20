from rest_framework.serializers import Serializer, CharField, UUIDField
from users_service.exceptions.service import ValidationException
from typing import Any
from uuid import UUID


class ProductAddRequestSerializer(Serializer):
    product_id = UUIDField(required=True)
    
    def validate_product_id(self, value: Any) -> UUID:
        if not isinstance(value, UUID):
            try:
                return UUID(value)
            except (ValueError, AttributeError):
                raise ValidationException(
                    detail=f"product_id '{value}' is not a valid uuid string"
                )
            except TypeError:
                raise ValidationException(
                    detail=f"product_id is required"
                )
        return value
    
    def validate(self, attrs: dict):
        self.product_id = self.validate_product_id(
            value=attrs.get("product_id")
        )
        return self


class PaginatedRequestSerializer(Serializer):
    page = CharField(required=True)
    page_size = CharField(required=True)

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

    def validate(self, attrs: dict):
        self.page = self.validate_paginator_parameter(
            value=attrs.get("page"),
            parameter="page"
        )
        self.page_size = self.validate_paginator_parameter(
            value=attrs.get("page_size"),
            parameter="page_size"
        )
        return self
