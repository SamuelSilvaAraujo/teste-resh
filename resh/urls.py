from django.urls import path, include

urlpatterns = [
    path('', include("core.urls", namespace="core")),
]
