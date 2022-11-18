from rest_framework.serializers import ModelSerializer

from products_service.models import Product
from products_service.mappers.models.category_mapper import CategoryMapper
from products_service.serializers.responses.category_response import CategorySerializer
from products_service.mappers.models.type_mapper import TypeMapper
from products_service.serializers.responses.type_response import TypeResponse
from products_service.mappers.models.brand_mapper import BrandMapper
from products_service.serializers.responses.brand_response import BrandSerializer

from uuid import UUID


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "characteristics": instance.characteristics,
            "category": self.prepapre_category(
                category_id=instance.category_id
            ).data,
            "brand": self.prepare_brand(
                brand_id=instance.brand_id
            ).data,
            "type": self.prepare_type(
                type_id=instance.type_id
            ).data
        }

    def prepapre_category(self, category_id: UUID) -> ModelSerializer:
        category = CategoryMapper.get_category_by_id(id=category_id)
        return CategorySerializer(instance=category)
    
    def prepare_type(self, type_id: UUID) -> ModelSerializer:
        type = TypeMapper.get_by_id(id=type_id)
        return TypeResponse(instance=type)

    def prepare_brand(self, brand_id: UUID) -> ModelSerializer:
        brand = BrandMapper.get_brand_by_id(id=brand_id)
        return BrandSerializer(instance=brand)
