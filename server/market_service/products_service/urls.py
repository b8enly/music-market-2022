from products_service.views.public.categories.details import (
    categories, categories_paginated
)
from products_service.views.public.brands.details import (
    brands, brands_paginated
)
from products_service.views.public.types.details import types

from django.urls import path

urlpatterns = [
    path("brands", brands),
    path("brands/list", brands_paginated),

    path("categories", categories),
    path("categories/list", categories_paginated),

    path("types", types)
]
