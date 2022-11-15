from products_service.models import Brand
from django.db.models import QuerySet


class BrandMapper:
    @staticmethod
    def find_brands_with_count(count: int) -> QuerySet:
        return Brand.objects.all()[:count]

    @staticmethod
    def find_all_brands() -> QuerySet:
        return Brand.objects.all()
