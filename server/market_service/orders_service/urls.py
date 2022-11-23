from orders_service.views.internal.delivery.details import delivery_methods
from orders_service.views.internal.pay.details import pay_methods

from django.urls import path

urlpatterns = [
    path("delivery_methods/", delivery_methods),
    path("pay_methods/", pay_methods),
]
