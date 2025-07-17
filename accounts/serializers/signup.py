from rest_framework import serializers
from django.core.exceptions import ValidationError

from accounts.models import User

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email')

        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError('User with the following Email already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user