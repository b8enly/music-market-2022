from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from products_service.models import Brand, Category, Product, Type
from uuid import UUID


class BrandMapper:
    @staticmethod
    def get_by_id(id: UUID) -> Brand:
        try:
            return Brand.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def find_all() -> QuerySet:
        return Brand.objects.all()

    @staticmethod
    def find_limited(limit: int) -> QuerySet:
        return Brand.objects.all()[:limit]


class CategoryMapper:
    @staticmethod
    def get_by_id(id: UUID) -> Category:
        try:
            return Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def find_all() -> QuerySet:
        return Category.objects.all()

    @staticmethod
    def find_limited(limit: int) -> QuerySet:
        return Category.objects.all()[:limit]


class ProductMapper:
    @staticmethod
    def get_by_id(id: UUID) -> Product:
        try:
            return Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    
    @staticmethod
    def find_by_category(category_id: UUID) -> QuerySet:
        return Product.objects.filter(category_id=category_id)


    @staticmethod
    def find_by_brand(brand_id: UUID) -> QuerySet:
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


class TypeMapper:
    @staticmethod
    def get_by_id(id: UUID) -> Type:
        try:
            return Type.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def find_limited(limit: int) -> QuerySet:
        return Type.objects.all()[:limit]
