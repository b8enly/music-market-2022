from django.urls import path, include

NAMESPACE = "users_service.routes"

urlpatterns = [
    path("", include(f"{NAMESPACE}.favorites")),
    path("", include(f"{NAMESPACE}.djoser")),
    path("", include(f"{NAMESPACE}.users")),
    path("", include(f"{NAMESPACE}.cart")),
]
