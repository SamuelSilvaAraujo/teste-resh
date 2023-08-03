from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.serializer import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
    ChangeEmailSerializer,
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

class ChangeEmailApiView(UpdateAPIView):
    """
    `api/change/email/` -- alterar email do usuário
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeEmailSerializer

    def get_object(self):
        return self.request.user
