from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.models.cart_mapper import CartMapper


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart(request: Request) -> Response:
    products = CartMapper.get_cart_products_by_user_id(user_id=request.data.get("user_id"))
    paginator = LimitOffsetPagination()
    result_list = paginator.paginate_queryset(products, request)
    return Response(data={
        "count": paginator.count,
        "next": paginator.get_next_link(),
        "previous": paginator.get_previous_link(),
        "page_size": len(result_list),
        "results": [
            {
                "user_id": request.data.get("user_id"),
                "products": list(map(lambda product: {
                    product.id
                }, result_list))
            }
        ]
    })