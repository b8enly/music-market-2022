from stocks_service.models import StockType, Stock, ProductOnSale
from django.contrib import admin


class StockTypeAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    pass


class ProductOnSaleAdmin(admin.ModelAdmin):
    pass


admin_models_map = [
    [StockType, StockTypeAdmin],
    [Stock, StockAdmin],
    [ProductOnSale, ProductOnSaleAdmin]
]

for admin_models in admin_models_map:
    admin.site.register(*admin_models)

