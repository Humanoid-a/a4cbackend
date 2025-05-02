from rest_framework import serializers

from .models import School
from .models import FrontendUser

class FrontendUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = FrontendUser
        fields = ['id', 'username', 'email', 'password', 'biography', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = FrontendUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

