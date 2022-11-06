from django.db import models
from random import randint
from uuid import uuid4


def gen_big_int():
    return randint(1_000_000_000, 9_999_999_999)


class PayMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=255, null=False, unique=True)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"


class DeliveryMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=255, null=False, unique=True)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"


class ProductSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.UUIDField(null=False)
    product_id = models.UUIDField(null=False)

    class Meta:
        unique_together = ("id", "user_id", "product_id")


class Order(models.Model):
    number = models.BigIntegerField(default=gen_big_int, unique=True)
    user_id = user_id = models.UUIDField(null=False)
    product_set = models.ForeignKey(
        to=ProductSet, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    payment_method = models.ForeignKey(
        to=PayMethod, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    delivery_method = models.ForeignKey(
        to=DeliveryMethod, 
        to_field="id", 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.number}"
