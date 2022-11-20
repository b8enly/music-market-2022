from users_service.views.public.users.details import detail
from users_service.views.public.users.mutations import (
    sign_out,
    sign_in, 
    sign_up, 
)

from django.urls import path


urlpatterns = [
    path("sign_up", sign_up),
    path("sign_in", sign_in),
    path("sign_out", sign_out),
    path("me", detail),
]
