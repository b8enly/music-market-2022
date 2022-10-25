from orders_service.models import PayMethod, Order, DeliveryMethod, ProductSet
from django.contrib import admin


class PayMethodAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class DeliveryMethodAdmin(admin.ModelAdmin):
    pass


class ProductSetAdmin(admin.ModelAdmin):
    pass


admin_models_map = [
    [PayMethod, PayMethodAdmin],
    [Order, OrderAdmin],
    [DeliveryMethod, DeliveryMethodAdmin],
    [ProductSet, ProductSetAdmin],
]

for admin_models in admin_models_map:
    admin.site.register(*admin_models)
