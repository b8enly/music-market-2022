from products_service.exceptions.service.validation_exception import (
    ValidationException
)
from rest_framework.serializers import Serializer, CharField
from typing import Any


class PaginatedRequest(Serializer):
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
