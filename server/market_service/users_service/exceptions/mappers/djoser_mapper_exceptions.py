from rest_framework.exceptions import APIException


class DjoserMapperRegistrException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperRegistrException: failed registr user\n{self.args}"


class DjoserMapperSignInException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperSignInException: failed sign in\n{self.args}"


class DjoserMapperSignOutException(Exception):
    def __str__(self) -> str:
        return f"DjoserMapperSignOutException: failed sign out\n{self.args}"


class DjoserMapperGetInfoException(APIException):
    def __str__(self) -> str:
        return f"{self.__class__}: failed get info about user\n{self.args}"
