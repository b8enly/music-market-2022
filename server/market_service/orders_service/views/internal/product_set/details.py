from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import DjangoPaginator
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.exceptions.service import ValidationException
from orders_service.mappers.models import ProductSetMapper
from orders_service.serializers.requests.orders import (
    ProductSetPaginatedRequestSerializer
)
from orders_service.serializers.responses.base import (
    PaginatedResponseSerializer
)

from uuid import UUID


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def paginate_product_set(request: Request, product_set_id: UUID) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = ProductSetPaginatedRequestSerializer().validate(
        attrs={
            "page": page,
            "page_size": page_size,
            "product_set_id": product_set_id
        }
    )

    products = ProductSetMapper.get_product_set_by_id(set_id=product_set_id)
    paginator = DjangoPaginator(
        object_list=list(map(lambda product: product.product_id, products)),
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    respomse_serializer = PaginatedResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=respomse_serializer.data)
