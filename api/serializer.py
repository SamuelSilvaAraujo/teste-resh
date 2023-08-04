from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate

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
            last_name=validated_data["last_name"],
            password=validated_data["password"],
            email=validated_data["email"],
            username=validated_data["email"],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, max_length=150)
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=200,
        min_length=8,
    )
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        return Token.objects.filter(user=self.usuario).latest("created").key

    def validate(self, data):
        print(data["username"])
        print(User.objects.all().values("username"))
        self.usuario = authenticate(
            username=data["username"],
            password=data["password"],
            request=self.context["request"],
        )
        if not self.usuario:
            raise AuthenticationFailed("Usuário ou senha incorreta")
        return data

    def save(self):
        Token.objects.create(user=self.usuario)


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "email",
            "name",
        ]
        read_only_fields = [
            "email",
        ]
    
    def get_name(self, obj):
        return obj.get_full_name()


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=200,
        min_length=8,
    )
    new_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=200,
        min_length=8,
    )
    

    class Meta:
        model = User
        fields = [
            "password",
            "new_password",
        ]
    
    def validate_password(self, value):
        if self.instance.check_password(value):
            return value
        raise serializers.ValidationError('Senha Inválida')

    def validate_new_password(self, value):
        validate_password(value, self.instance)
        return value
    
    def save(self, **kwargs):
        self.instance.set_password(self.validated_data['new_password'])
        self.instance.save(update_fields=['password'])
        return self.instance


class ChangeEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
        ]

    def save(self, **kwargs):
        self.instance.email = self.validated_data["email"]
        self.instance.username = self.validated_data["email"]
        self.instance.save(update_fields=['email', 'username'])
        return self.instance
