from users_service.views.internal.favorites.mutations import add_to_favorites, delete_from_favorites
from users_service.views.internal.favorites.details import favorites

from django.urls import path

urlpatterns = [
    path("favorites/add/", add_to_favorites),
    path("favorites/", favorites),
    path("favorites/delete/", delete_from_favorites)
]
