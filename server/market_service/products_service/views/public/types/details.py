from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.serializers.responses.types_response import TypesResponse
from products_service.serializers.requests.types_linit_request import (
    TypesLimitRequest
)
from products_service.mappers.models.type_mapper import TypeMapper


ALLOWED_METHODS = ["GET"]

DEFAULT_CATEGORIES_COUNT = 3


@api_view(ALLOWED_METHODS)
def types(request: Request) -> Response:
    query_count = request.query_params.get("count")
    json_count = request.data.get("count")
    count = (
        (DEFAULT_CATEGORIES_COUNT if json_count is None else json_count)
        if query_count is None else query_count
    )

    request_serializer = TypesLimitRequest().validate(attrs={
        "count": count
    })

    types = TypeMapper.find_limit_types(count=request_serializer.count)
    response_serializer = TypesResponse(types, many=True)

    return Response(data={
        "types": response_serializer.data
    })
