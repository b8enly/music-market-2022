from django.db import models
from uuid import uuid4


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    file_id = models.TextField(null=False)
    type = models.TextField(max_length=20, null=False)
    source_id = models.UUIDField(null=False)

    class Meta:
        unique_together = ("file_id", "source_id")
