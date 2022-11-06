from users_service.models import User, Cart, Favorites
from django.contrib.admin import ModelAdmin, register


@register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        "id",
        "email",
        "name",
        "surname",
    )

    fields = (
        "name",
        "surname",
        "patronymic",
        "address",
        "is_staff",
    )


@register(Favorites)
class FavoriteAdmin(ModelAdmin):
    list_display = (
        "user",
        "product_id",
    )

    readonly_fields = (
        "id",
        "user",
        "product_id",
    )


@register(Cart)
class CartAdmin(ModelAdmin):
    list_display = (
        "user",
        "product_id",
    )

    readonly_fields = (
        "id",
        "user",
        "product_id",
    )
