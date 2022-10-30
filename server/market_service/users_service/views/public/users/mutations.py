import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.models.users_mapper import UsersMapper


@api_view(["POST"])
def sign_up(request: Request) -> Response:
    response = requests.post(url="http://127.0.0.1:8000/api/users/auth/users/", data=request.data)
    if response.status_code == 201:
        user = UsersMapper.get_user_by_id(response.json()["id"])
        user.name = request.data["name"]
        user.surname = request.data["surname"]
        user.patronymic = request.data["patronymic"]
        user.address = request.data["address"]
        user.save()
        return Response(data={
            "success": True
        })
    else:
        return Response(response.json())


@api_view(["POST"])
def sign_in(request: Request) -> Response:
    response_json = requests.post(url="http://127.0.0.1:8000/api/users/auth/token/login/", data=request.data).json()
    return Response(data={
        "token": response_json["auth_token"]
    })


@api_view(["GET"])
def sign_out(request: Request, id: str) -> Response:
    requests.post(url="http://127.0.0.1:8000/api/users/auth/token/logout/",
                  headers={"Authorization": request.headers["Authorization"]})
    return Response()
