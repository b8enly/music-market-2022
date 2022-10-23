from django.contrib import admin
from products_service.models import Category, Type, Product


class CategoryAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin_models_map = [
    [Category, CategoryAdmin],
    [Type, TypeAdmin],
    [Product, ProductAdmin]
]

for admin_models in admin_models_map:
    admin.site.register(*admin_models)

