from django.urls import path, include

from api.views import (
    RegisterApiView,
    LoginApiView,
    ProfileApiView,
    ChangePasswordApiView,
    ChangeUserApiView,
    LogoutApiView,
)

app_name = "api"


urlpatterns = [
    path(
        "",
        include(
            [
                path("register/", RegisterApiView.as_view(), name="register"),
                path("login/", LoginApiView.as_view(), name="login"),
                path("logout/", LogoutApiView.as_view(), name="logout"),
                path("profile/", ProfileApiView.as_view(), name="profile"),
                path(
                    "change/",
                    include(
                        [
                            path(
                                "password/",
                                ChangePasswordApiView.as_view(),
                                name="change_password",
                            ),
                            path(
                                "user/",
                                ChangeUserApiView.as_view(),
                                name="change_user",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    )
]
