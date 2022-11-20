class DjoserMapperRegistrException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperRegistrException: failed registr user\n{self.args}"


class DjoserMapperSignInException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperSignInException: failed sign in\n{self.args}"


class DjoserMapperSignOutException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperSignOutException: failed sign out\n{self.args}"


class DjoserMapperGetInfoException(Exception):
    def __str__(self) -> str:
        return f"{self.__class__}: failed get info about user\n{self.args}"


class UserMapperUpdateException(Exception):
    def __str__(self) -> str:
        return f"failed update user:\n{self.args}"


class FavoriteMapperCreateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if "UNIQUE constraint failed" in self.args[0][0]:
            self.args = ("product already in favorites",)

    def __str__(self) -> str:
        return f"{self.__class__}: failed create favorite\n{self.args}"
