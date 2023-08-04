from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from rest_framework.generics import (
    CreateAPIView,
    RetrieveDestroyAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from api.serializer import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
    ChangeUserSerializer,
)
from api.throttles import RegisterThrottle


class RegisterApiView(CreateAPIView):
    """
    `api/register/` -- registar um novo usuário
    """

    serializer_class = RegisterSerializer
    throttle_classes = [RegisterThrottle]


class LoginApiView(CreateAPIView):
    """
    `api/login/` -- login do usuário
    """

    serializer_class = LoginSerializer


class ProfileApiView(RetrieveDestroyAPIView):
    """
    `api/profile/` -- perfil do usuário
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordApiView(UpdateAPIView):
    """
    `api/change/password/` -- alterar senha do usuário
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class ChangeUserApiView(UpdateAPIView):
    """
    `api/change/user/` -- alterar o usuário
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeUserSerializer

    def get_object(self):
        return self.request.user


class LogoutApiView(DestroyAPIView):
    """
    `api/logout/` -- logout do usuário
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(Token, user=self.request.user)
