from products_service.exceptions.service.validation_exception import (
    ValidationException
)
from rest_framework.serializers import Serializer, CharField


class LimitRequest(Serializer):
    count = CharField(required=True)

    def validate_count(self, value) -> None:
        if isinstance(value, int):
            return
        if isinstance(value, str):
            if not value.isdigit():
                raise ValidationException(
                    detail="count parameter must be an integer"
                )
            self.count = int(value)
        return ValidationException(detail="count parameter is reequired")
    
    def validate(self, attrs):
        self.validate_count(attrs.get("count"))
        return self
