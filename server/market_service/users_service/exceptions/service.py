from rest_framework.exceptions import APIException
from rest_framework.exceptions import status


class NotFountException(APIException):
    status_code = status.HTTP_404_NOT_FOUND


class ValidationException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class BadRequestExcpetion(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
