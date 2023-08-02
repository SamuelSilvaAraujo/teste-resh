from django.urls import path

from core.views import ProfileView, LoginView, RegisterView

app_name = "core"

urlpatterns = [
    path('', ProfileView.as_view(), name="profile"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
]