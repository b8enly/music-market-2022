import requests

from products_service.exceptions.mappers import (
    UsersServiceMapperInternalException
)
from uuid import UUID


class UsersServiceMapper:
    BASE_URL = "http://127.0.0.1:8000/api/users/internal"

    @staticmethod
    def add_to_favorites(token: str, product_id: UUID) -> bool:
        response = requests.post(
            url=f"{UsersServiceMapper.BASE_URL}/favorites/add",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "product_id": product_id
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return True

    @staticmethod
    def add_to_cart(token: str, product_id: UUID) -> bool:
        response = requests.post(
            url=f"{UsersServiceMapper.BASE_URL}/cart/add",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "product_id": product_id
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return True

    @staticmethod
    def paginate_favorites_by_auth_token(
        token: str, 
        page: int, 
        page_size: int
    ) -> dict:
        response = requests.get(
            url=f"{UsersServiceMapper.BASE_URL}/favorites",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "page": page,
                "page_size": page_size
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return response.json()

    @staticmethod
    def paginate_cart_products_by_auth_token(
        token: str, 
        page: int, 
        page_size: int
    ) -> dict:
        response = requests.get(
            url=f"{UsersServiceMapper.BASE_URL}/cart",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "page": page,
                "page_size": page_size
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return response.json()

    @staticmethod
    def delete_from_favorites(token: str, product_id: UUID) -> bool:
        response = requests.delete(
            url=f"{UsersServiceMapper.BASE_URL}/favorites/delete",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "product_id": product_id
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return True

    @staticmethod
    def delete_from_cart(token: str, product_id: UUID) -> bool:
        response = requests.delete(
            url=f"{UsersServiceMapper.BASE_URL}/cart/delete",
            headers={
                "Authorization": f"Token {token}"
            },
            data={
                "product_id": product_id
            }
        )

        if not response.ok:
            raise UsersServiceMapperInternalException(response.json())
        
        return True
