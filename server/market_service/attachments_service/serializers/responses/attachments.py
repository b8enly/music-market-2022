from rest_framework.serializers import Serializer, ModelSerializer
from attachments_service.models import Attachment


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"


class AttachmentsResponseSerializer(Serializer):
    def __init__(self, attachments: dict):
        self._data = {}

        for source_id in attachments:
            self._data[str(source_id)] = {}
            
            for source_type in attachments[source_id]:
                self._data[str(source_id)][source_type] = []

                for attachment in attachments[source_id][source_type]:
                    self._data[str(source_id)][source_type].append(
                        AttachmentSerializer(instance=attachment).data
                    )        

    @property
    def data(self):
        return self._data
