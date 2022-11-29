from orders_service.views.public.pay.details import pay_methods
from django.urls import path

urlpatterns = [
    path("payment_methods", pay_methods),
]
