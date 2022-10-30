from users_service.models import User


class UsersMapper:
    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        return User.objects.get(id=user_id)
