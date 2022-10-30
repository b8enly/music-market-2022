import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from users_service.mappers.models.users_mapper import UsersMapper


@api_view(["GET"])
def detail(request: Request) -> Response:
    response_json = requests.get("http://127.0.0.1:8000/api/users/auth/users/me/",
                                 headers={"Authorization": request.headers["Authorization"]}).json()
    user = UsersMapper.get_user_by_id(response_json["id"])
    return Response(data={
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "patronymic": user.patronymic,
        "address": user.address
    })
