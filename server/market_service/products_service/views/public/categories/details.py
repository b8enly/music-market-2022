from rest_framework.pagination import DjangoPaginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.serializers.requests.categories_paginated_request import (
    CategoriesPaginatedRequest
)
from products_service.serializers.requests.categories_limit_request import (
    CategoriesLimitRequest
)
from products_service.mappers.models.category_mapper import CategoryMapper
from products_service.serializers.responses.categories_response import (
    CategoryResponse
)
from products_service.serializers.responses.paginated_response import (
    PaginatedResponse
)
from products_service.exceptions.service.internal_exception import (
    InternalException
)


ALLOWED_METHODS = ["GET"]

DEFAULT_CATEGORIES_COUNT = 3


@api_view(ALLOWED_METHODS)
def categories(request: Request) -> Response:
    query_count = request.query_params.get("count")
    json_count = request.data.get("count")
    count = (
        (DEFAULT_CATEGORIES_COUNT if json_count is None else json_count)
        if query_count is None else query_count
    )

    request_serializer = CategoriesLimitRequest().validate(attrs={
        "count": count
    })

    categories = CategoryMapper.find_limit_categories(
        count=request_serializer.count
    )
    response_serializer = CategoryResponse(categories, many=True)

    return Response(data={
        "categories": response_serializer.data
    })


@api_view(ALLOWED_METHODS)
def categories_paginated(request: Request) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = CategoriesPaginatedRequest().validate(attrs={
        "page": page,
        "page_size": page_size
    })

    categories = CategoryMapper.find_all_categories()
    paginator = DjangoPaginator(
        object_list=categories,
        per_page=request_serializer.page_size
    )

    if paginator.num_pages < request_serializer.page:
        raise InternalException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )
    
    return Response(data=PaginatedResponse(
        paginator=paginator,
        page_number=request_serializer.page,
        serializer=CategoryResponse
    ).data())
