from rest_framework import serializers
from .models import MenuModel, CategoryModel, MenuItemModel
from django_tenants.routers import TenantSyncRouter


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = [
            'id',
            'name',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'name',
        ]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemModel
        fields = [
            'id',
            'name',
            'description',
        ]