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
    serializer_class = RegisterSerializer
    throttle_classes = [RegisterThrottle]


class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer


class ProfileApiView(RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

class ChangeEmailApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeEmailSerializer

    def get_object(self):
        return self.request.user
