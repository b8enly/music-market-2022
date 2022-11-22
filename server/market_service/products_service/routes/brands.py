from products_service.views.public.brands.details import (
    brands_paginated,
    brands
)
from django.urls import path

urlpatterns = [
    path(
        route="brands", 
        view=brands
    ),
    path(
        route="brands/list", 
        view=brands_paginated
    ),
]
