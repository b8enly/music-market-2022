from rest_framework.serializers import ModelSerializer
from products_service.models import Brand


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
