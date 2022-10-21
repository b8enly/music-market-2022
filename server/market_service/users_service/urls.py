from django.urls import path, include, re_path
from .views.public.users.mutations import create_user

urlpatterns = [
    path('sign_in/', create_user),
    path('auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken'))
]
