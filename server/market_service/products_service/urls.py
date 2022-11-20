from django.urls import path, include

NAMESPACE = "products_service.routes"

urlpatterns = [
    path("", include(f"{NAMESPACE}.categories")),
    path("", include(f"{NAMESPACE}.products")),
    path("", include(f"{NAMESPACE}.brands")),
    path("", include(f"{NAMESPACE}.types")),
]
