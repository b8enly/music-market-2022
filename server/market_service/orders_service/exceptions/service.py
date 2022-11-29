from rest_framework.exceptions import APIException
from rest_framework import status


class ValidationException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND


class BadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST