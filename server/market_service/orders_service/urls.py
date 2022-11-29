from django.urls import path, include

NAMESPACE = "orders_service.routes"

urlpatterns = [
    path("", include(f"{NAMESPACE}.orders")),
    path("", include(f"{NAMESPACE}.payment_methods")),
    path("", include(f"{NAMESPACE}.delivery_methods")),
    path("", include(f"{NAMESPACE}.product_set")),
]
