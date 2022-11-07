from orders_service.models import PayMethod, Order, DeliveryMethod, ProductSet
from django.contrib.admin import register, ModelAdmin


@register(PayMethod)
class PayMethodAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    readonly_fields = (
        "id",
    )


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        "number",
        "user_id",
    )

    readonly_fields = (
        "number",
    )


@register(DeliveryMethod)
class DeliveryMethodAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    readonly_fields = (
        "id",
    )


@register(ProductSet)
class ProductSetAdmin(ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "product_id",
    )

    readonly_fields = (
        "id",
    )
