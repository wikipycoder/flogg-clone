from rest_framework.serializers import ModelSerializer
from .models import User


class RegistraterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
    
    extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):

        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

