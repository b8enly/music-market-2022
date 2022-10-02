from django.urls import path
from .views.public.users.mutations import create_user

urlpatterns = [
    path('sign_up/', create_user)
]
