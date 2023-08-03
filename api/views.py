from rest_framework.generics import CreateAPIView

from api.serializer import RegisterSerializer

class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerializer
