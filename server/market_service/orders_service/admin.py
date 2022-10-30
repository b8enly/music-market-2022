from orders_service.models import PayMethod, Order, DeliveryMethod, ProductSet
from django.contrib.admin import register, ModelAdmin


@register(PayMethod)
class PayMethodAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    pass


@register(DeliveryMethod)
class DeliveryMethodAdmin(ModelAdmin):
    pass


@register(ProductSet)
class ProductSetAdmin(ModelAdmin):
    pass
