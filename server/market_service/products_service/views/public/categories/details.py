from rest_framework.pagination import DjangoPaginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.exceptions.service import ValidationException
from products_service.serializers.responses.categories import (
    CategoriesPaginatedResponseSerializer,
    CategoriesLimitResponseSerializer,
)
from products_service.serializers.requests.categories import (
    CategoriesPaginatedRequestSerializer,
    CategoriesLimitRequestSerializer,
)
from products_service.mappers.models import CategoryMapper


ALLOWED_METHODS = ["GET"]

DEFAULT_BRANDS_COUNT = 3


@api_view(ALLOWED_METHODS)
def categories(request: Request) -> Response:
    query_count = request.query_params.get("count")
    json_count = request.data.get("count")
    count = (
        (DEFAULT_BRANDS_COUNT if json_count is None else json_count)
        if query_count is None else query_count
    )

    request_serializer = CategoriesLimitRequestSerializer().validate(attrs={
        "count": count
    })

    categories = CategoryMapper.find_limited(limit=request_serializer.count)

    response_serializer = CategoriesLimitResponseSerializer(
        instance=categories,
        many=True
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def categories_paginated(request: Request) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = CategoriesPaginatedRequestSerializer().validate(
        attrs={
            "page": page,
            "page_size": page_size
        }
    )

    categories = CategoryMapper.find_all()
    paginator = DjangoPaginator(
        object_list=categories, 
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = CategoriesPaginatedResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)
