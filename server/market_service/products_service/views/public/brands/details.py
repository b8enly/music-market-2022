from rest_framework.pagination import DjangoPaginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.exceptions.service import ValidationException
from products_service.serializers.responses.brands import (
    BrandPaginatedResponseSerializer,
    BrandLimitResponseSerializer,
)
from products_service.serializers.requests.brands import (
    BrandsPaginatedRequestSerializer,
    BrandsLimitRequestSerializer,
)
from products_service.mappers.models import BrandMapper


ALLOWED_METHODS = ["GET"]

DEFAULT_BRANDS_COUNT = 3


@api_view(ALLOWED_METHODS)
def brands(request: Request) -> Response:
    query_count = request.query_params.get("count")
    json_count = request.data.get("count")
    count = (
        (DEFAULT_BRANDS_COUNT if json_count is None else json_count)
        if query_count is None else query_count
    )

    request_serializer = BrandsLimitRequestSerializer().validate(attrs={
        "count": count
    })

    brands = BrandMapper.find_limited(limit=request_serializer.count)

    response_serializer = BrandLimitResponseSerializer(
        instance=brands, 
        many=True
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def brands_paginated(request: Request) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = BrandsPaginatedRequestSerializer().validate(attrs={
        "page": page,
        "page_size": page_size
    })

    brands = BrandMapper.find_all()
    paginator = DjangoPaginator(
        object_list=brands, 
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = BrandPaginatedResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)
