from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedDefaultRouter, NestedSimpleRouter
from .views import MenuViewSet, RestaurantViewSet, CategoryViewSet, MenuItemViewSet

#
# router = DefaultRouter()
# router.register('restaurants', RestaurantViewSet)
#
# menu_router = NestedDefaultRouter(router, 'restaurants', lookup='restaurant')
# menu_router.register('menus', MenuViewSet)
#
# category_router = NestedDefaultRouter(menu_router, 'menus', lookup='menu')
# category_router.register('categories', CategoryViewSet)
#
# item_router = NestedDefaultRouter(category_router, 'categories', lookup='category')
# item_router.register('items', MenuItemViewSet)

router = SimpleRouter()
router.register('restaurants', RestaurantViewSet)

menu_router = NestedSimpleRouter(router, 'restaurants', lookup='restaurant')
menu_router.register('menus', MenuViewSet)

category_router = NestedSimpleRouter(menu_router, 'menus', lookup='menu')
category_router.register('categories', CategoryViewSet)

item_router = NestedSimpleRouter(category_router, 'categories', lookup='category')
item_router.register('items', MenuItemViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('', include(menu_router.urls)),
    url('', include(category_router.urls)),
    url('', include(item_router.urls)),
]
