from users_service.views.internal.cart.details import cart
from users_service.views.internal.cart.mutations import (
    delete_from_cart,
    add_to_cart,
    flush_cart,
)
from django.urls import path

urlpatterns = [
    path(
        route="internal/cart/add",
        view=add_to_cart
    ),
    path(
        route="internal/cart/delete",
        view=delete_from_cart
    ),
    path(
        route="internal/cart",
        view=cart
    ),
    path(
        route="internal/cart/flush",
        view=flush_cart
    ),
]
