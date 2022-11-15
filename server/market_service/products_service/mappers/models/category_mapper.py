from products_service.models import Category
from django.db.models import QuerySet


class CategoryMapper:
    @staticmethod
    def find_limit_categories(count: int) -> QuerySet:
        return Category.objects.all()[:count]

    @staticmethod
    def find_all_categories() -> QuerySet:
        return Category.objects.all()
