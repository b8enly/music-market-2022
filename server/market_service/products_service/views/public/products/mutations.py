from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.exceptions.service import BadRequestException
from products_service.mappers.services import UsersServiceMapper
from products_service.serializers.requests.products import (
    ProductAddToFavoriteRequestSerializer
)
from products_service.exceptions.mappers import (
    UsersServiceMapperInternalException
)

from uuid import UUID


@api_view(["POST", "DELETE"])
@permission_classes([IsAuthenticated])
def favorites_mutations(request: Request, product_id: UUID) -> Response:
    def add_to_favorites(token: str) -> Response:
        try:
            result = UsersServiceMapper.add_to_favorites(
                token=token, 
                product_id=product_id
            )
        except UsersServiceMapperInternalException as e:
            raise BadRequestException(detail=e.args)

        return Response(data={
            "success": result
        })

    def delete_from_favorites(token: str) -> Response:
        try:
            result = UsersServiceMapper.delete_from_favorites(
                token=token,
                product_id=product_id
            )
        except UsersServiceMapperInternalException as e:
            raise BadRequestException(detail=e.args)

        return Response(data={
            "success": result
        })

    token = request.headers.get("Authorization").split()[1]

    request_serializer = ProductAddToFavoriteRequestSerializer().validate(
        attrs={
            "product_id": product_id
        }
    )

    if request.method == "POST":
        return add_to_favorites(
            token=token
        )
    if request.method == "DELETE":
        return delete_from_favorites(
            token=token
        )


@api_view(["POST", "DELETE"])
@permission_classes([IsAuthenticated])
def cart_mutations(request: Request, product_id: UUID) -> Response:
    def add_to_cart(token: str) -> bool:
        return UsersServiceMapper.add_to_cart(
            token=token, 
            product_id=product_id
        )
    
    def delete_from_cart(token: str) -> bool:
        return UsersServiceMapper.delete_from_cart(
            token=token,
            product_id=product_id
        )

    try:
        token = request.headers.get("Authorization").split()[1]

        if request.method == "POST":
            result = add_to_cart(token=token)
        if request.method == "DELETE":
            result = delete_from_cart(token=token)
    except UsersServiceMapperInternalException as e:
        raise BadRequestException(detail=e.args)
    
    return Response(data={
        "success": result
    })
