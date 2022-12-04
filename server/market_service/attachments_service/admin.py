from attachments_service.models import Attachment
from django.contrib.admin import ModelAdmin, register


@register(Attachment)
class MediaAttachmentAdmin(ModelAdmin):
    list_display = (
        "id",
        "type",
        "file_id",
        "source_id",
    )
