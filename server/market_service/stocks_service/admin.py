from stocks_service.models import StockType, Stock, ProductOnSale
from django.contrib.admin import ModelAdmin, register


@register(StockType)
class StockTypeAdmin(ModelAdmin):
    pass


@register(Stock)
class StockAdmin(ModelAdmin):
    pass


@register(ProductOnSale)
class ProductOnSaleAdmin(ModelAdmin):
    pass
