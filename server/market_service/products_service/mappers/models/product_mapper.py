from products_service.models import Product
from django.db.models import QuerySet
from uuid import UUID


class ProductMapper:
    @staticmethod
    def find_products_by_category(category_id: UUID) -> QuerySet:
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def find_products_by_brand(brand_id: UUID) -> QuerySet:
        return Product.objects.filter(brand_id=brand_id)

    @staticmethod
    def find_by_category_and_type(
        category_id: UUID, 
        type_id: UUID
    ) -> QuerySet:
        return Product.objects.filter(category_id=category_id, type_id=type_id)

    @staticmethod
    def find_by_brand_and_type(
        brand_id: UUID,
        type_id: UUID
    ) -> QuerySet:
        return Product.objects.filter(brand_id=brand_id, type_id=type_id)

    @staticmethod
    def get_by_id(id: UUID) -> Product:
        return Product.objects.get(id=id)
