from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.exceptions.mappers import MapperCreateException
from users_service.exceptions.service import BadRequestExcpetion
from users_service.mappers.services import DjoserMapper
from users_service.serializers.requests.cart import (
    CartDeleteRequestSerializer,
    CartAddRequestSerializer,
)
from users_service.mappers.models import CartMapper


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request: Request) -> Response:
    token = request.headers.get("Authorization").split()[1]
    user_info = DjoserMapper.get_me(auth_token=token)

    request_serializer = CartAddRequestSerializer().validate(attrs={
        "product_id": request.data.get("product_id")
    })

    try:
        CartMapper.create(
            user_id=user_info.get("id"),
            product_id=request_serializer.product_id
        )
    except MapperCreateException as e:
        raise BadRequestExcpetion(detail=e.args)

    return Response(data={
        "success": True
    })


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_from_cart(request: Request) -> Response:
    token = request.headers.get("Authorization").split()[1]
    user_info = DjoserMapper.get_me(auth_token=token)

    request_serializer = CartDeleteRequestSerializer().validate(attrs={
        "user_id": user_info.get("id"),
        "product_id": request.data.get("product_id")
    })

    CartMapper.delete(
        user_id=request_serializer.user_id,
        product_id=request_serializer.product_id
    )

    return Response(data={
        "success": True
    })
