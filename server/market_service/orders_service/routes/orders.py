
from orders_service.views.public.orders.details import (
    order_detail,
    orders_list, 
)
# from django.urls import path

# urlpatterns = [
#     path("public/list/", orders_list),
#     path("public/details/", order_detail),
from orders_service.views.public.orders.mutations import checkout
from django.urls import path

urlpatterns = [
    path(
        route="checkout", 
        view=checkout
    ),
    
    path(
        route="",
        view=orders_list
    ),
    
    path(
        route="<int:order_number>",
        view=order_detail
    ),
]
