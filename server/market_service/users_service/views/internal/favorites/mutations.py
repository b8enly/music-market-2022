from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.models.favorites_mapper import FavoritesMapper


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_favorites(request: Request) -> Response:
    FavoritesMapper.create(
        user_id=request.data.get("user_id"),
        product_id=request.data.get("product_id")
    )

    return Response(data={
        "success": True
    })


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_from_favorites(request: Request) -> Response:
    FavoritesMappers.delete(
        user_id=request.data.get("user_id"),
        product_id=request.data.get("product_id")
    )

    return Response(data={
        "success": True
    }
    )
