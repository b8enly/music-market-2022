from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from attachments_service.serializers.responses.attachments import (
    AttachmentsResponseSerializer
)
from attachments_service.serializers.requests.attachments import (
    AttachmentsRequestSerializer
)
from attachments_service.mappers.models import AttachmentsMapper


@api_view(["GET"])
def attachments(request: Request) -> Response:
    print(request.data)

    req = dict(request.data)

    print(req)

    request_serializer = AttachmentsRequestSerializer().validate(attrs={
        "source_ids": req.get("source_ids")
    })

    media_attachments = AttachmentsMapper.find_images_and_videos_by_source(
        source_ids=request_serializer.source_ids
    )

    response_serializer = AttachmentsResponseSerializer(
        attachments=media_attachments
    )

    return Response(data=response_serializer.data)
