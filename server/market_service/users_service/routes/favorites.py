from users_service.views.internal.favorites.details import favorites
from users_service.views.internal.favorites.mutations import (
    delete_from_favorites,
    add_to_favorites,
)
from django.urls import path

urlpatterns = [
    path(
        route="internal/favorites/add",
        view=add_to_favorites
    ),
    path(
        route="internal/favorites/delete",
        view=delete_from_favorites
    ),
    path(
        route="internal/favorites",
        view=favorites
    ),
]
