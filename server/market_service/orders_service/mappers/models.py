from orders_service.models import PayMethod, DeliveryMethod
from django.db.models import QuerySet


class PayMethodMapper:
    @staticmethod
    def get() -> QuerySet[PayMethod]:
        return PayMethod.objects.all()


class DeliveryMethodMapper:
    @staticmethod
    def get() -> QuerySet[DeliveryMethod]:
        return DeliveryMethod.objects.all()
