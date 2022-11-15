from rest_framework.serializers import ModelSerializer
from products_service.models import Type


class TypesResponse(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
