from products_service.exceptions.service import ValidationException
from rest_framework.serializers import Serializer, CharField
from typing import Any


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


class LimitRequestSerializer(Serializer):
    count = CharField(required=True)

    def validate_count(self, value: Any) -> int:
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            if not value.isdigit():
                raise ValidationException(
                    detail="count parameter must be an integer"
                )
            return int(value)
    
    def validate(self, attrs):
        self.count = self.validate_count(attrs.get("count"))
        return self
