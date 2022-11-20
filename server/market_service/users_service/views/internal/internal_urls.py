from users_service.views.internal.cart.mutations import add_to_cart, delete_from_cart
from users_service.views.internal.cart.details import cart

from django.urls import path

urlpatterns = [
    path("cart/add/", add_to_cart),
    path("cart/", cart),
    path("cart/delete/", delete_from_cart)
]
