from users_service.exceptions.service import ValidationException
from users_service.serializers.requests.base import (
    ProductAddRequestSerializer,
    PaginatedRequestSerializer,
)
from users_service.mappers.models import CartMapper

from rest_framework.serializers import UUIDField
from typing import Any
from uuid import UUID


class CartAddRequestSerializer(ProductAddRequestSerializer):
    pass


class CartDeleteRequestSerializer(CartAddRequestSerializer):
    user_id = UUIDField(required=True)

    def validate_product_id(self, value: Any) -> UUID:
        return super().validate_product_id(value)
    
    def validate(self, attrs: dict):
        super().validate(attrs=attrs)
        self.user_id = attrs.get("user_id")
        if not CartMapper.get_by_user_id_and_product_id(
            user_id=self.user_id,
            product_id=self.product_id
        ):
            raise ValidationException(detail=f"product not in favorites" )
        return self


class CartPaginatedRequestSerializer(PaginatedRequestSerializer):
    pass
