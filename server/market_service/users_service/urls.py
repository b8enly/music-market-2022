from django.urls import path, include, re_path
from users_service.views.public.users.mutations import sign_up, sign_in, sign_out
from users_service.views.public.users.details import detail

urlpatterns = [
    path("sign_up/", sign_up),
    path("sign_in/", sign_in),
    path("<str:id>/sign_out/", sign_out),
    path("user/", detail),
    path("auth/", include("djoser.urls")),
    re_path(r"auth/", include("djoser.urls.authtoken"))
]
