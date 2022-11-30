from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.mappers.models import PayMethodMapper


@api_view(["GET"])
def pay_methods(request: Request) -> Response:
    pay_methods = PayMethodMapper.get()
    return Response(data=list(map(lambda pay_method: {
        "name": pay_method.name,
        "id": pay_method.id
    }, pay_methods)))
