from rest_framework.serializers import Serializer
from rest_framework.serializers import ListField

from attachments_service.exceptions.service import ValidationException
from typing import Any
from uuid import UUID


def validate_uuid(value: Any, param: str) -> UUID:
    if not isinstance(value, UUID):
        try:
            return UUID(value)
        except (TypeError, ValueError, AttributeError) as e:
            raise ValidationException(
                detail=f"{param} is not a valid uuid string"
            )
    return value


class AttachmentsRequestSerializer(Serializer):
    source_id = ListField(required=True)

    def validate_source_ids(self, value: Any) -> UUID:
        if value is None:
            raise ValidationException(detail="source_ids is required")
        if not isinstance(value, list):
            raise ValidationException(detail="source_ids must be a list")
        return list(map(
            lambda val: validate_uuid(
                value=val,
                param=f"source_ids.{value.index(val)}"
            ), value
        ))
    
    def validate(self, attrs: dict):
        self.source_ids = self.validate_source_ids(
            value=attrs.get("source_ids")
        )
        return self
