from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import DjangoPaginator
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.serializers.requests.orders import (
    OrdersPaginatedRequestSerializer
)
from orders_service.mappers.models import ProductSetMapper
from orders_service.mappers.models import OrdersMapper

from users_service.mappers.services import DjoserMapper


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def orders_list(request: Request) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = OrdersPaginatedRequestSerializer().validate(attrs={
        "page": page,
        "page_size": page_size
    })

    user_info = DjoserMapper.get_me(
        auth_token=request.headers.get("Authorization").split()[1]
    )

    orders = OrdersMapper.get_orders_by_user_id(user_id=user_info.get("id"))
    paginator = DjangoPaginator(
        object_list=orders,
        per_page=request_serializer.page_size
    )
    page = paginator.get_page(request_serializer.page)
    return Response(
        data={
            "count": paginator.count,
            "next": (
                None if not page.has_next() 
                else page.next_page_number()
            ),
            "previous": (
                None if not page.has_previous() 
                else page.previous_page_number()
            ),
            "page_size": request_serializer.page_size,
            "result": list(map(lambda order: {
                "order_number": order.number,
                "payment_method_id": order.payment_method.id,
                "delivety_method_id": order.delivery_method.id,
                "product_set_id": order.product_set
            }, page.object_list))
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_detail(request: Request, order_number: int) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = OrdersPaginatedRequestSerializer().validate(attrs={
        "page": page,
        "page_size": page_size
    })

    order = OrdersMapper.get_order_by_number(number=order_number)
    product_sets = ProductSetMapper.get_product_set_by_id(set_id=order.product_set)
    paginator = DjangoPaginator(
        object_list=product_sets,
        per_page=request_serializer.page_size
    )
    page = paginator.get_page(request_serializer.page)

    return Response(
        data={
            "payment_method_id": order.payment_method.id,
            "delivery_method_id": order.delivery_method.id,
            "count": paginator.count,
            "next": (
                None if not page.has_next() 
                else page.next_page_number()
            ),
            "previous": (
                None if not page.has_previous() 
                else page.previous_page_number()
            ),
            "page_size": request_serializer.page_size,
            "products_ids": list(map(lambda set_item: {
                set_item.product_id,
            }, page.object_list))
        }
    )
