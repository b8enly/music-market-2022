from django.utils import timezone
from django.db import models

from uuid import uuid4


def next_day():
    return timezone.now() + timezone.timedelta(days=1)


class StockType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(max_length=255, null=False)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"


class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = models.ForeignKey(
        to=StockType, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    name = models.TextField(max_length=255, null=False)
    description = models.TextField(max_length=1000, null=True)
    active_from = models.DateTimeField(default=timezone.now)
    active_to = models.DateTimeField(default=next_day)

    def __str__(self) -> str:
        return f"{str(self.id)[:4]} {self.name}"


class ProductOnSale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    stock = models.ForeignKey(
        to=Stock, 
        to_field="id", 
        on_delete=models.CASCADE
    )
    product_id = models.UUIDField(null=False)

    class Meta:
        unique_together = ("id", "stock", "product_id")
