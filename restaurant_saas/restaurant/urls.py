from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import MenuViewSet, RestaurantViewSet, CategoryViewSet, MenuItemViewSet

router = DefaultRouter()

# router.register('menus', MenuViewSet)
router.register('restaurants', RestaurantViewSet)

# restaurant_router = NestedDefaultRouter(router, 'restaurants', lookup='owner_id')
# restaurant_router.register('menus', MenuViewSet)

menu_router = NestedDefaultRouter(router, 'restaurants', lookup='restaurant_id')
menu_router.register('menus', MenuViewSet)

category_router = NestedDefaultRouter(menu_router, 'menus', lookup='menu_id')
category_router.register('categories', CategoryViewSet)

item_router = NestedDefaultRouter(category_router, 'categories', lookup='category_id')
item_router.register('items', MenuItemViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('', include(menu_router.urls)),
    url('', include(category_router.urls)),
    url('', include(item_router.urls)),
]
