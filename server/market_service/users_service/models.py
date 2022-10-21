from django.db import models
from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, null=False, unique=True)
    name = models.TextField(max_length=255, null=True)
    surname = models.TextField(max_length=255, null=True)
    patronymic = models.TextField(max_length=255, null=True)
    address = models.JSONField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        unique_together = ('id', 'email')


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
