from rest_framework import serializers
from users_service.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = (
            "id",
            "email",
            "name",
            "surname",
            "address",
        )