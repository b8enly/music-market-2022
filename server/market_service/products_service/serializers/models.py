from products_service.mappers.services import AttachmentsServiceMapper
from products_service.models import Brand, Type, Category, Product
from products_service.mappers.models import (
    CategoryMapper, 
    BrandMapper, 
    TypeMapper
)

from rest_framework.serializers import ModelSerializer
from uuid import UUID


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
    

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, media, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self._data = {}
        self.media = media
    
    def to_representation(self, instance: Product) -> dict:
        self._data.update({
            "id": instance.id,
            "name": instance.name,
            "price": instance.price,
            "media": self.media.get(str(instance.id))
        })
        return self._data
    
    def get_category(self, category_id: UUID) -> dict:
        category = CategoryMapper.get_by_id(id=category_id)
        return CategorySerializer(instance=category).data
    
    def get_brand(self, brand_id: UUID) -> dict:
        brand = BrandMapper.get_by_id(id=brand_id)
        return BrandSerializer(instance=brand).data
    
    def get_type(self, type_id: UUID) -> dict:
        type = TypeMapper.get_by_id(id=type_id)
        return TypeSerializer(instance=type).data


class CategoryProductSerializer(ProductSerializer):
    def __init__(self, media, instance=None, data=..., **kwargs):
        super().__init__(media, instance, data, **kwargs)

    def to_representation(self, instance: Product):
        data = super().to_representation(instance=instance)
        data["brand"] = self.get_brand(brand_id=instance.brand.id)
        return data


class ProductDetailSerializer(ProductSerializer):
    def __init__(self, media, instance=None, data=..., **kwargs):
        super().__init__(media, instance, data, **kwargs)
    
    def to_representation(self, instance: Product) -> dict:
        data = super().to_representation(instance)
        data["description"] = instance.description
        data["amount"] = instance.amount
        data["characteristics"] = instance.characteristics
        data["category"] = self.get_category(category_id=instance.category.id)
        data["brand"] = self.get_brand(brand_id=instance.brand.id)
        data["type"] = self.get_type(type_id=instance.type.id)
        return data
