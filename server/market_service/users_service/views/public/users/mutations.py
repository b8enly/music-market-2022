from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.exceptions.mappers.djoser_mapper_exceptions import (
    DjoserMapperSignOutException,
    DjoserMapperRegistrException,
    DjoserMapperSignInException,
)
from users_service.exceptions.mappers.user_mapper_exceptions import (
    UserMapperUpdateException
)
from users_service.mappers.services.djoser_mapper import DjoserMapper
from users_service.mappers.models.users_mapper import UsersMapper
from users_service.serializers import UserModelSerializer

from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID


@api_view(["POST"])
def sign_up(request: Request) -> Response:
    try:
        registered_user = DjoserMapper.sign_up(
            email=request.data.pop("email"),
            password=request.data.pop("password")
        )

        user_id = registered_user.get("id")
        UsersMapper.update_user_by_id(id=user_id, **request.data)
        user = UsersMapper.get_user_by_id(user_id=user_id)

        return Response(data=UserModelSerializer(user).data)
    
    except DjoserMapperRegistrException as e:
        return Response(
            data={
                "error": "failed register user",
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

    except UserMapperUpdateException as e:
        return Response(
            data={
                "error": "failed fill user",
                "details": e.args
            },
            status=400
        )


@api_view(["POST"])
def sign_in(request: Request) -> Response:
    try:
        response = DjoserMapper.sign_in(
            email=request.data.get("email"),
            password=request.data.get("password")
        )

        return Response(data={
            "token": response.get("auth_token")
        })
    
    except DjoserMapperSignInException as e:
        return Response(
            data={
                "error": "failed sign in",
                "detail": e.args
            },
            status=400
        )


@api_view(["GET"])
def sign_out(request: Request, user_id: UUID) -> Response:
    try:
        return Response(data={
            "success": DjoserMapper.sign_out(
                auth_token=request.headers.get("Authorization")
            )
        })
    except DjoserMapperSignOutException as e:
        return Response(
            data={
                "error": f"failed sign out for user {user_id}",
                "details": e.args
            },
            status=400
        )