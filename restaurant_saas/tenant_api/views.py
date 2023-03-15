from django.shortcuts import render
# from .serializers import MenuSerializer, CategorySerializer, MenuItemSerializer
from rest_framework.decorators import action
from rest_framework.routers import SimpleRouter

from rest_framework.generics import RetrieveAPIView
from restaurant.models import MenuModel, CategoryModel, MenuItemModel
from restaurant.views import MenuViewSet
from .serializers import TenantMenuSerializer
from restaurant.serializers import MenuSerializer


class TenantMenuView(RetrieveAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = TenantMenuSerializer
    lookup_field = 'id'
