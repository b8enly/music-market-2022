from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.TextField(max_length=500, null=False)
    name = models.TextField(max_length=255, null=True)
    surname = models.TextField(max_length=255, null=True)
    patronymic = models.TextField(max_length=255, null=True)
    address = models.JSONField(null=True)

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
