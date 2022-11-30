from orders_service.views.internal.product_set.details import (
    paginate_product_set
)
from django.urls import path


urlpatterns = [
    path(
        route="internal/product_set/<uuid:product_set_id>",
        view=paginate_product_set,
    )
]
