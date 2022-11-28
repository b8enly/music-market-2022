from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from orders_service.mappers.models import ProductSetMapper
from orders_service.mappers.models import OrdersMapper

from users_service.mappers.services import DjoserMapper


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def orders_list(request: Request) -> Response:
    user_info = DjoserMapper.get_me(
        auth_token=request.headers.get("Authorization").split()[1]
    )

    orders = OrdersMapper.get_orders_by_user_id(user_id=user_info.get("id"))
    paginator = LimitOffsetPagination()
    result_page = paginator.paginate_queryset(orders, request)
    return Response(
        data={
            "count": paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "page_size": len(result_page),
            "result": list(map(lambda order: {
                "order_number": order.number,
                "payment_method_id": order.payment_method.id,
                "delivety_method_id": order.delivery_method.id,
                "product_set_id": order.product_set.product_set_id
            }, result_page))
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_detail(request: Request) -> Response:
    order = OrdersMapper.get_order_by_number(request.data.get("order_number"))
    product_sets = ProductSetMapper.get_product_set_by_id(set_id=order.product_set.product_set_id)
    paginator = LimitOffsetPagination()
    result_page = paginator.paginate_queryset(product_sets, request)

    return Response(
        data={
            "payment_method_id": order.payment_method.id,
            "delivery_method_id": order.delivery_method.id,
            "count": paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "page_size": len(result_page),
            "products_ids": list(map(lambda set: {
                set.product_id,
            }, result_page))
        }
    )
