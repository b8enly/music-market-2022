from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import DjangoPaginator
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.exceptions.mapper import UserServiceMapperInternalException
from orders_service.exceptions.service import BadRequestException
from orders_service.mappers.services import UsersServiceMapper
from orders_service.serializers.requests.orders import (
    OrderCheckoutRequestSerializer
)
from orders_service.serializers.models import (
    OrderSerializer
)
from orders_service.mappers.models import (
    DeliveryMethodMapper,
    ProductSetMapper,
    PayMethodMapper,
    OrderMapper,
)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def checkout(request: Request) -> Response:
    delivery_method = request.data.get("delivery_method")
    payment_method = request.data.get("payment_method")
    product_ids = request.data.get("product_ids")
    auth_token = request.headers.get("Authorization").split()[1]

    request_serializer = OrderCheckoutRequestSerializer().validate(attrs={
        "delivery_method": delivery_method,
        "payment_method": payment_method,
        "product_ids": product_ids
    })

    user_info = UsersServiceMapper.get_user_by_auth_token(
        auth_token=auth_token
    )
    user_id = user_info.get("id")

    product_set_id = ProductSetMapper.create(
        user_id=user_id,
        product_ids=request_serializer.product_ids
    )

    payment_method = PayMethodMapper.get_by_id(
        id=request_serializer.payment_method
    )

    delivery_method = DeliveryMethodMapper.get_by_id(
        id=request_serializer.delivery_method
    )

    order = OrderMapper.create(
        user_id=user_id,
        product_set_id=product_set_id,
        payment_method_id=payment_method,
        delivery_method_id=delivery_method
    )

    try:
        UsersServiceMapper.flush_cart_for_user(auth_token=auth_token)
    except UserServiceMapperInternalException as e:
        raise BadRequestException(detail=e.args)

    response_serializer = OrderSerializer(instance=[order], many=True)

    return Response(data=response_serializer.data)
