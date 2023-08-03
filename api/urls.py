from django.urls import path, include

from api.views import RegisterApiView

app_name = "api"


urlpatterns = [
    path("", include([
        path("register/", RegisterApiView.as_view(), name="register"),
    ]))
]
