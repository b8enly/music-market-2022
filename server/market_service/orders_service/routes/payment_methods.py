from orders_service.views.public.pay.details import pay_methods
from django.urls import path

urlpatterns = [
    path("public/pay_methods/", pay_methods),
]
