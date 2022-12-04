from django.urls import path, include

urlpatterns = [
    path("", include("attachments_service.routes.attachments")),    
]
