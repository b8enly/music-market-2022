from products_service.models import Category
from django.db.models import QuerySet
from uuid import UUID


class CategoryMapper:
    @staticmethod
    def get_category_by_id(id: UUID) -> Category:
        return Category.objects.get(id=id)
