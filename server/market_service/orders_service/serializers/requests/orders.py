from orders_service.serializers.requests.base import (
    PaginatedRequestSerializer
)
from orders_service.exceptions.service import (
    ValidationException, 
    NotFoundException,
)
from orders_service.mappers.models import (
    DeliveryMethodMapper,
    ProductSetMapper,
    PayMethodMapper,
)

from rest_framework.serializers import Serializer, UUIDField, ListField
from typing import Any
from uuid import UUID


def validate_uuid(value: Any, param: str) -> UUID:
    if not isinstance(value, UUID):
        try:
            return UUID(value)
        except (TypeError, ValueError) as e:
            raise ValidationException(detail=f"{param} is not a valid uuid string")
    return value


def is_transferred(value: Any, param: str) -> bool:
    if value is None:
        raise ValidationException(detail=f"{param} is required")
    return True


class OrderCheckoutRequestSerializer(Serializer):
    delivery_method = UUIDField(required=True)
    payment_method = UUIDField(required=True)
    product_ids = ListField(required=True)

    def validate_delivery_method(self, value) -> UUID:
        if is_transferred(value=value, param="delivery_method"):
            value = validate_uuid(value=value, param="delivery_method")
            if not DeliveryMethodMapper.get_by_id(id=value):
                raise NotFoundException(detail="delivery method not found")
            return value

    def validate_payment_method(self, value) -> UUID:
        if is_transferred(value=value, param="payment_method"):
            value = validate_uuid(value=value, param="payment_method")
            if not PayMethodMapper.get_by_id(id=value):
                raise NotFoundException(detail="payment method not found")
            return value
    
    def validate_products_ids(self, value) -> list:
        if is_transferred(value=value, param="product_ids"):
            if not isinstance(value, list):
                raise ValidationException(detail="product_ids must be a list")
            return list(map(
                lambda val: validate_uuid(
                    value=val, 
                    param=f"product_ids.{value.index(val)}"
                ), 
                value
            ))
    
    def validate(self, attrs):
        self.delivery_method = self.validate_delivery_method(
            value=attrs.get("delivery_method")
        )
        self.payment_method = self.validate_payment_method(
            value=attrs.get("payment_method")
        )
        self.product_ids = self.validate_products_ids(
            value=attrs.get("product_ids")
        )
        return self
        

class OrdersPaginatedRequestSerializer(PaginatedRequestSerializer):
    pass


class ProductSetPaginatedRequestSerializer(PaginatedRequestSerializer):
    product_set_id = UUIDField(required=True)

    def validate_product_set_id(self, value: UUID) -> UUID:
        if len(ProductSetMapper.get_product_set_by_id(set_id=value)) == 0:
            raise NotFoundException(
                detail=f"product set with id {value} not found"
            )
        return value
    
    def validate(self, attrs: dict):
        super().validate(attrs)
        self.product_set_id = self.validate_product_set_id(
            value=attrs.get("product_set_id")
        )
        return self
