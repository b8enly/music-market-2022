from orders_service.views.public.delivery.details import delivery_methods
from django.urls import path

urlpatterns = [
    path("public/delivery_methods/", delivery_methods),
]
