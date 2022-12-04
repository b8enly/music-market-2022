from attachments_service.models import Attachment
from uuid import UUID


class AttachmentsMapper:
    @staticmethod
    def find_images_and_videos_by_source(source_ids: list[UUID]) -> dict:
        attachments = Attachment.objects.filter(
            source_id__in=source_ids,
            type__in=["image", "video"]
        )

        sources_attachments = {}

        for source_id in source_ids:
            source_attachments = attachments.all().filter(source_id=source_id)

            sources_attachments[source_id] = {
                "image": [],
                "video": [],
            }

            for attachment in source_attachments:
                sources_attachments[attachment.source_id][attachment.type] \
                    .append(attachment)


        return sources_attachments