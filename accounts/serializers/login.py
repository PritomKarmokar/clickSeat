from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=5, max_length=255)