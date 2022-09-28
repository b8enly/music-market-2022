from django.db import models
from uuid import uuid4


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = models.TextField(max_length=30, null=False)
    size = models.IntegerField(null=False)
    path = models.URLField(null=False)


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    media_id = models.ForeignKey(
        to=Media, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    media_type = models.TextField(max_length=30, null=False)
    source_id = models.UUIDField(null=False)
    source_type = models.TextField(max_length=30, null=False)
