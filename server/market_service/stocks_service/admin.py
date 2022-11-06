from stocks_service.models import StockType, Stock, ProductOnSale
from django.contrib.admin import ModelAdmin, register


@register(StockType)
class StockTypeAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    readonly_fields = (
        "id",
    )


@register(Stock)
class StockAdmin(ModelAdmin):
    list_display = (
        "id",
        "type",
        "name"
    )

    readonly_fields = (
        "id",
    )


@register(ProductOnSale)
class ProductOnSaleAdmin(ModelAdmin):
    list_display = (
        "id",
        "stock",
        "product_id",
    )

    readonly_fields = (
        "id",
    )
