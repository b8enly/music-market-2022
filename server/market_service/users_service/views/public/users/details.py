from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.exceptions.mappers.djoser_mapper_exceptions import (
    DjoserMapperGetInfoException
)
from users_service.mappers.services.djoser_mapper import DjoserMapper
from users_service.mappers.models.users_mapper import UsersMapper
from users_service.serializers import UserModelSerializer

from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID


@api_view(["GET"])
def detail(request: Request, user_id: UUID) -> Response:
    try:
        user_info = DjoserMapper.get_me(
            auth_token=request.headers.get("Authorization")
        )
        user = UsersMapper.get_user_by_id(user_id=user_info.get("id"))
    
        return Response(data=UserModelSerializer(user).data)

    except DjoserMapperGetInfoException as e:
        return Response(
            data={
                "error": f"failed get info about user {user_id}",
                "details": e.args
            },
            status=400
        )

    except (ObjectDoesNotExist, ValueError) as e:
        return Response(
            data={
                "error": "failed get user",
                "details": e.args
            },
            status=400
        )
