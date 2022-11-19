from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.serializers.responses.types import (
    TypesLimitResponseSerializer
)
from products_service.serializers.requests.types import (
    TypesLimitRequestSerializer
)
from products_service.mappers.models import TypeMapper


ALLOWED_METHODS = ["GET"]

DEFAULT_BRANDS_COUNT = 3


@api_view(ALLOWED_METHODS)
def types(request: Request) -> Response:
    query_count = request.query_params.get("count")
    json_count = request.data.get("count")
    count = (
        (DEFAULT_BRANDS_COUNT if json_count is None else json_count)
        if query_count is None else query_count
    )

    request_serializer = TypesLimitRequestSerializer().validate(attrs={
        "count": count
    })

    types = TypeMapper.find_limited(limit=request_serializer.count)

    response_serializer = TypesLimitResponseSerializer(
        instance=types,
        many=True
    )

    return Response(data=response_serializer.data)
