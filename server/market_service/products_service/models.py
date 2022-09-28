from django.db import models
from uuid import uuid4


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=255, null=False)


class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(to=Category, to_field="id", on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=False)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(to=Category, to_field="id", on_delete=models.CASCADE)
    type = models.ForeignKey(to=Type, to_field="id", on_delete=models.CASCADE)
    brand = models.TextField(max_length=255, null=False)
    name = models.TextField(max_length=255, null=False)
    description = models.TextField(max_length=1000, null=True)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    characteristics = models.JSONField(null=True)
