from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import DjangoPaginator
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.exceptions.service import ValidationException
from users_service.mappers.services import DjoserMapper
from users_service.serializers.responses.cart import (
    CartPaginatedResponseSerializer
)
from users_service.serializers.requests.cart import (
    CartPaginatedRequestSerializer
)
from users_service.mappers.models import CartMapper


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart(request: Request) -> Response:
    user_info = DjoserMapper.get_me(
        auth_token=request.headers.get("Authorization").split()[1]
    )

    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = CartPaginatedRequestSerializer().validate(attrs={
        "page": page,
        "page_size": page_size
    })

    products_in_cart = CartMapper.find_by_user_id(user_id=user_info.get("id"))
    paginator = DjangoPaginator(
        object_list=products_in_cart,
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        ) 

    response_serializer = CartPaginatedResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page_size
    )

    return Response(data=response_serializer.data)
