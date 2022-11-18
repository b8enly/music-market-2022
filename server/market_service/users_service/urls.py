from django.urls import path, include

urlpatterns = [
    path("internal/", include("users_service.views.internal.internal_urls"))
]
