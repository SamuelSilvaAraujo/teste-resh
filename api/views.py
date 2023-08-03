from rest_framework.generics import CreateAPIView

from api.serializer import RegisterSerializer, LoginSerializer
from api.throttles import RegisterThrottle


class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerializer
    throttle_classes = [RegisterThrottle]


class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer
