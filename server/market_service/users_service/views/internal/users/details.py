from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.services import DjoserMapper


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request: Request) -> Response:
    token = request.headers.get("Authorization").split()[1]

    user_info = DjoserMapper.get_me(auth_token=token)

    return Response(data=user_info)
