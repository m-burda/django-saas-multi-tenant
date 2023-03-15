from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TenantMenuView

router = SimpleRouter()

urlpatterns = [
    path("menus/<int:id>", TenantMenuView.as_view()),
]
