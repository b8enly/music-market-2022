from attachments_service.views.internal.attachments.details import attachments
from django.urls import path

urlpatterns = [
    path(
        route="internal/source",
        view=attachments
    )
]
