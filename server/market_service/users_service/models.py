from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users_service.managers import CustomUserManager
from uuid import uuid4


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    name = models.TextField(max_length=255, null=True)
    surname = models.TextField(max_length=255, null=True)
    patronymic = models.TextField(max_length=255, null=True)
    address = models.JSONField(null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        unique_together = ('id', 'email')

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name} {self.surname}"


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(to=User, to_field="id", on_delete=models.CASCADE)
    product_id = models.UUIDField(null=False)

    class Meta:
        unique_together = ('user', 'product_id')


class Favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(to=User, to_field="id", on_delete=models.CASCADE)
    product_id = models.UUIDField(null=False)

    class Meta:
        unique_together = ('user', 'product_id')
