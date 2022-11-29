import requests

from orders_service.exceptions.mapper import UserServiceMapperInternalException


class UsersServiceMapper:
    BASE_URL = "http://127.0.0.1:8000/api/users/internal"

    @staticmethod
    def get_user_by_auth_token(auth_token: str) -> dict:
        response = requests.get(
            url=f"{UsersServiceMapper.BASE_URL}/me",
            headers={
                "Authorization": f"Token {auth_token}"
            }
        )

        if not response.ok:
            raise UserServiceMapperInternalException(response.json())

        return response.json()

    @staticmethod
    def flush_cart_for_user(auth_token: str) -> bool:
        response = requests.delete(
            url=f"{UsersServiceMapper.BASE_URL}/cart/flush",
            headers={
                "Authorization": f"Token {auth_token}"
            }
        )

        if not response.ok:
            raise UserServiceMapperInternalException(response.json())

        return True
