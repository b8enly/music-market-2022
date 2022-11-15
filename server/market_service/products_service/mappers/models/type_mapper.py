from products_service.models import Type
from django.db.models import QuerySet


class TypeMapper:
    @staticmethod
    def find_limit_types(count: int) -> QuerySet:
        return Type.objects.all()[:count]
