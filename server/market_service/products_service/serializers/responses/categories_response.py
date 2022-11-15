from rest_framework.serializers import ModelSerializer
from products_service.models import Category


class CategoryResponse(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
