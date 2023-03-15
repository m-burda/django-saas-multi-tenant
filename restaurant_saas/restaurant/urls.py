from django.urls import include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import MenuViewSet, RestaurantViewSet, CategoryViewSet, MenuItemViewSet

router = SimpleRouter()
router.register("restaurants", RestaurantViewSet)

menu_router = NestedSimpleRouter(router, "restaurants", lookup="restaurant")
menu_router.register("menus", MenuViewSet)

category_router = NestedSimpleRouter(menu_router, "menus", lookup="menu")
category_router.register("categories", CategoryViewSet)

item_router = NestedSimpleRouter(category_router, "categories", lookup="category")
item_router.register("items", MenuItemViewSet)

urlpatterns = [
    url("", include(router.urls)),
    url("", include(menu_router.urls)),
    url("", include(category_router.urls)),
    url("", include(item_router.urls)),
]
