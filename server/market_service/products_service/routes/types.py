from products_service.views.public.types.details import types
from django.urls import path


urlpatterns = [
    path(
        route="types",
        view=types
    ),
]
