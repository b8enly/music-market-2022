from products_service.models import Category, Brand, Type
from products_service.serializers.responses.base import (
    PaginatedResponseSerializer
)
from products_service.serializers.models import (
    CategoryProductSerializer, 
    ProductDetailSerializer,
    CategorySerializer, 
    ProductSerializer, 
    BrandSerializer, 
    TypeSerializer
)

from rest_framework.pagination import DjangoPaginator
from rest_framework.serializers import Serializer

from django.db.models import QuerySet


class CategoryProductsResponseSerializer(PaginatedResponseSerializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int, 
        category: Category
    ):
        super().__init__(paginator, page_number)
        self._data["category"] = CategorySerializer(instance=category).data
        self._data["results"] = CategoryProductSerializer(
            instance=self.page.object_list,
            many=True
        ).data


class ProductsPaginatedResponseSerializer(PaginatedResponseSerializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        super().__init__(paginator, page_number)
        self._data["results"] = ProductSerializer(
            instance=self.page.object_list,
            many=True
        ).data


class BrandProductsResponseSerializer(PaginatedResponseSerializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int,
        brand: Brand
    ):
        super().__init__(paginator, page_number)
        self._data["brand"] = BrandSerializer(instance=brand).data
        self._data["results"] = ProductSerializer(
            instance=self.page.object_list,
            many=True
        ).data


class CategoryTypeProductsResponseSerializer(
    CategoryProductsResponseSerializer
):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int, 
        category: Category,
        type: Type
    ):
        super().__init__(paginator, page_number, category)
        self._data["type"] = TypeSerializer(instance=type).data


class BrandTypeProductsResponseSerializer(BrandProductsResponseSerializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int, 
        brand: Brand,
        type: Type
    ):
        super().__init__(paginator, page_number, brand)
        self._data["type"] = TypeSerializer(instance=type).data


class ProductDetailResponseSerializer(ProductDetailSerializer):
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)


class FavoriteProductsResponseSerializer(Serializer):
    def __init__(
        self, 
        count: int, 
        next_page: int, 
        previous: int, 
        page_size: int,
        favorites: QuerySet
    ) -> None:
        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "favorites": ProductSerializer(instance=favorites, many=True).data
        }


class CartProductsResponseSerializer(Serializer):
    def __init__(
        self, 
        count: int, 
        next_page: int, 
        previous: int, 
        page_size: int, 
        cart: QuerySet
    ) -> None:
        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "cart": ProductSerializer(instance=cart, many=True).data
        }


class OrderProductsResponseSerializer(Serializer):
    def __init__(
        self,
        count: int, 
        next_page: int, 
        previous: int, 
        page_size: int, 
        product_set: QuerySet
    ) -> None:
        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "product_set": ProductSerializer(
                instance=product_set, 
                many=True
            ).data
        }
