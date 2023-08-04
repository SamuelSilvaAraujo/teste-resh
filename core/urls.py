from django.urls import include, path

from core.views import (
    ProfileView,
    LoginView,
    RegisterView,
    ChangeUserView,
)

app_name = "core"

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "change/",
        include(
            [
                path("user/", ChangeUserView.as_view(), name="change_user"),
            ]
        ),
    ),
]
