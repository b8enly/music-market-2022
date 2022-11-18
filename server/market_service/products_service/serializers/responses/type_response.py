from rest_framework.serializers import ModelSerializer
from products_service.models import Type


class TypeResponse(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
