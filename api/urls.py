from django.urls import path, include

from api.views import RegisterApiView, LoginApiView

app_name = "api"


urlpatterns = [
    path("", include([
        path("register/", RegisterApiView.as_view(), name="register"),
        path("login/", LoginApiView.as_view(), name="login"),
    ]))
]
