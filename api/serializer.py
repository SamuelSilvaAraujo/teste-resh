from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, max_length=200, write_only=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
        ]

    @transaction.atomic
    def create(self, validated_data):
        return User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data['last_name'],
            password=validated_data["password"],
            email=validated_data["email"],
        )
