from products_service.mappers.services import AttachmentsServiceMapper
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

        images = AttachmentsServiceMapper.get_images_by_source(
            source_ids=list(map(
                lambda product: product.id, 
                self.page.object_list
            ))
        )

        self._data["results"] = CategoryProductSerializer(
            media=images,
            instance=self.page.object_list,
            many=True
        ).data


class ProductsPaginatedResponseSerializer(PaginatedResponseSerializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        super().__init__(paginator, page_number)

        images = AttachmentsServiceMapper.get_images_by_source(
            source_ids=list(map(
                lambda product: product.id, 
                self.page.object_list
            ))
        )

        self._data["results"] = ProductSerializer(
            media=images,
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

        images = AttachmentsServiceMapper.get_images_by_source(
            source_ids=list(map(
                lambda product: product.id, 
                self.page.object_list
            ))
        )

        self._data["results"] = ProductSerializer(
            media=images,
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
    def __init__(self, media, instance=None, data=..., **kwargs):
        media = AttachmentsServiceMapper.get_attachments_by_source(source_ids=[instance[0].id])

        super().__init__(media, instance, data, **kwargs)


class FavoriteProductsResponseSerializer(Serializer):
    def __init__(
        self, 
        count: int, 
        next_page: int, 
        previous: int, 
        page_size: int,
        favorites: QuerySet
    ) -> None:
        if len(favorites) > 0:
            images = AttachmentsServiceMapper.get_images_by_source(
                source_ids=list(map(
                    lambda product: product.id, 
                    favorites
                ))
            )
        else:
            images = None

        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "favorites": ProductSerializer(media=images, instance=favorites, many=True).data
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
        if len(cart) > 0:
            images = AttachmentsServiceMapper.get_images_by_source(
                source_ids=list(map(
                    lambda product: product.id, 
                    cart
                ))
            )
        else:
            images = None

        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "cart": ProductSerializer(media=images, instance=cart, many=True).data
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
        images = AttachmentsServiceMapper.get_images_by_source(
            source_ids=list(map(
                lambda product: product.id, 
                product_set
            ))
        )

        self._data = {
            "count": count,
            "next": next_page,
            "previous": previous,
            "page_size": page_size,
            "product_set": ProductSerializer(
                media=images,
                instance=product_set, 
                many=True
            ).data
        }
