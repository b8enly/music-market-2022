from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.mappers.models import DeliveryMethodMapper


@api_view(["GET"])
def delivery_methods(request: Request) -> Response:
    delivery_methods = DeliveryMethodMapper.get()
    return Response(data=list(map(lambda delivery_method: {
        "name": delivery_method.name,
        "id": delivery_method.id
    }, delivery_methods)))
