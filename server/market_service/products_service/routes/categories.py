from products_service.views.public.categories.details import (
    categories_paginated,
    categories, 
)
from django.urls import path


urlpatterns = [
    path(
        route="categories", 
        views=categories
    ),
    path(
        route="categories/list", 
        view=categories_paginated
    ),
]
