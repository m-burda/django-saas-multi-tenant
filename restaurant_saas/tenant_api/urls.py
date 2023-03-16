from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TenantMenuView, TenantCategoryView, TenantItemView

router = SimpleRouter()

urlpatterns = [
    path("menus/<int:id>", TenantMenuView.as_view()),
    path("categories/<int:id>", TenantCategoryView.as_view()),
    path("items/<int:id>", TenantItemView.as_view()),
]
