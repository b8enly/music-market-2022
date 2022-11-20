from users_service.serializers.requests.base import PaginatedRequestSerializer
from users_service.exceptions.service import ValidationException
from users_service.mappers.models import FavoritesMapper

from rest_framework.serializers import Serializer, UUIDField
from typing import Any
from uuid import UUID


class FavoritesAddRequestSerializer(Serializer):
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


class FavoritesDeleteRequestSerializer(FavoritesAddRequestSerializer):
    user_id = UUIDField(required=True)

    def validate_product_id(self, value: Any) -> UUID:
        return super().validate_product_id(value)
    
    def validate(self, attrs: dict):
        super().validate(attrs=attrs)
        self.user_id = attrs.get("user_id")
        if not FavoritesMapper.get_by_user_id_and_product_id(
            user_id=self.user_id,
            product_id=self.product_id
        ):
            raise ValidationException(detail=f"product not in favorites" )
        return self


class FavoritesPaginatedRequestSerializer(PaginatedRequestSerializer):
    pass
