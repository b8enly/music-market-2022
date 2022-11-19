from products_service.views.public.products.details import (
    category_type_products,
    brand_type_products,
    category_products,
    brand_products,
    product_detail,
)

from django.urls import path

urlpatterns = [
    path(
        route="categories/<uuid:category_id>/products", 
        view=category_products
    ),
    path(
        route="brands/<uuid:brand_id>/products", 
        view=brand_products
    ),
    path(
        route="categories/<uuid:category_id>/types/<uuid:type_id>/products", 
        view=category_type_products
    ),
    path(
        route="brands/<uuid:brand_id>/types/<uuid:type_id>/products",
        view=brand_type_products
    ),
    path(
        route="<uuid:product_id>",
        view=product_detail
    )
]
