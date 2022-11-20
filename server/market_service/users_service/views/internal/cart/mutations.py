from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.models.cart_mapper import CartMapper


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request: Request) -> Response:
    CartMapper.create(
        user_id=request.data.get("user_id"),
        product_id=request.data.get("product_id")
    )

    return Response(data={
        "success": True
    })


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_from_cart(request: Request) -> Response:
    CartMapper.delete(
        user_id=request.data.get("user_id"),
        product_id=request.data.get("product_id")
    )

    return Response(data={
        "success": True
    }
    )
