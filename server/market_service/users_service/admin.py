from django.contrib import admin
from users_service.models import User, Cart, Favorites


class UserAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    pass


class FavoriteAdmin(admin.ModelAdmin):
    pass


admin_models_map = [
    [User, UserAdmin],
    [Cart, CartAdmin],
    [Favorites, FavoriteAdmin]
]

for admin_model in admin_models_map:
    admin.site.register(*admin_model)

