from django.urls import path, include
from users.views import CreateUserAPIView

urlpatterns = [
    path("", include("rest_framework.urls")),
    path("api/", include("tenant_api.urls")),
    path("register/", CreateUserAPIView.as_view()),
]
