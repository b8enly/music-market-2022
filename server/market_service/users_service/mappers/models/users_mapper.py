from users_service.exceptions.mappers.user_mapper_exceptions import (
    UserMapperUpdateException
)
from users_service.models import User

from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID


class UsersMapper:
    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        return User.objects.get(id=UUID(user_id))

    @staticmethod
    def get_user_by_uuid(id: UUID) -> User:
        return User.objects.get(id=id)

    @staticmethod
    def update_user_by_id(id: str, **update_fields: dict) -> int:
        try:
            return User.objects.filter(id=UUID(id)).update(**update_fields)
        except (ObjectDoesNotExist, ValueError) as e:
            raise UserMapperUpdateException(e.args)
