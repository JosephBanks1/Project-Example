from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ["id", "setup", "delivery", "creator"]

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ["id", "url", "creator"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)