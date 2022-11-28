from orders_service.views.public.orders.details import orders_list, order_detail
from django.urls import path

urlpatterns = [
    path("public/list/", orders_list),
    path("public/details/", order_detail),
]
