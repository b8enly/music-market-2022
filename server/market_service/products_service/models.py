from django.db import models
from uuid import uuid4


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=30, null=False)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"


class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(
        to=Category, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    name = models.TextField(max_length=30, null=False)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=30, null=False)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(
        to=Category, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(to=Type, to_field="id", on_delete=models.CASCADE)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, null=False)
    description = models.TextField(max_length=1000, null=True)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    characteristics = models.JSONField(null=True)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"
