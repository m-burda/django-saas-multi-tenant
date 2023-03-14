from rest_framework import serializers
from .models import MenuModel, CategoryModel, MenuItemModel
from django_tenants.routers import TenantSyncRouter


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemModel
        fields = '__all__'
