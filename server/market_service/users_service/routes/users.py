from users_service.views.internal.users.details import get_user_info
from users_service.views.public.users.details import detail
from users_service.views.public.users.mutations import (
    sign_out,
    sign_in, 
    sign_up, 
)

from django.urls import path


urlpatterns = [
    path(
        route="sign_up", 
        view=sign_up
    ),
    path(
        route="sign_in", 
        view=sign_in
    ),
    path(
        route="sign_out", 
        view=sign_out
    ),
    path(
        route="me", 
        view=detail
    ),

    path(
        route="internal/me",
        view=get_user_info
    )
]
