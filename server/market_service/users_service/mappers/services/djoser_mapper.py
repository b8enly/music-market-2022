import requests

from users_service.exceptions.mappers.djoser_mapper_exceptions import (
    DjoserMapperGetInfoException,
    DjoserMapperSignOutException,
    DjoserMapperRegistrException,
    DjoserMapperSignInException,
)


class DjoserMapper:
    BASE_URL = "http://127.0.0.1:8000/api/users/auth"

    @staticmethod
    def sign_up(email: str, password: str) -> dict:
        response = requests.post(
            url=f"{DjoserMapper.BASE_URL}/users/",
            data={
                "email": email,
                "password": password,
            }
        )
        
        if not response.ok:
            raise DjoserMapperRegistrException(response.json())

        return response.json()

    @staticmethod
    def sign_in(email: str, password: str) -> dict:
        response = requests.post(
            url=f"{DjoserMapper.BASE_URL}/token/login",
            data={
                "email": email,
                "password": password
            }
        )

        if not response.ok:
            raise DjoserMapperSignInException(response.json())
        
        return response.json()

    @staticmethod
    def sign_out(auth_token: str) -> bool:
        response = requests.post(
            url=f"{DjoserMapper.BASE_URL}/token/logout",
            headers={
                "Authorization": f"Token {auth_token}"
            }
        )

        if not response.ok:
            raise DjoserMapperSignOutException(response.json())
        
        return True

    @staticmethod
    def get_me(auth_token: str) -> dict:
        response = requests.get(
            url=f"{DjoserMapper.BASE_URL}/users/me",
            headers={
                "Authorization": f"Token {auth_token}"
            }
        )

        if not response.ok:
            raise DjoserMapperGetInfoException(response.json())

        return response.json()
