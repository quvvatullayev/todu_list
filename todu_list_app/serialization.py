from rest_framework import serializers
from .models import User, Todu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todu
        fields = '__all__'