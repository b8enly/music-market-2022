from products_service.models import Category, Type, Product, Brand
from django.contrib.admin import ModelAdmin, register


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id", 
        "name",
    )


@register(Type)
class TypeAdmin(ModelAdmin):
    list_display = (
        "id", 
        "name",
    )


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "category",
        "type",
        "brand",
        "name",
        "price",
        "amount",
    )


@register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = (
        "id", 
        "name",
    )
