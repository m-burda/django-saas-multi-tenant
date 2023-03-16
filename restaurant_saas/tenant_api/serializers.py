from rest_framework import serializers
from restaurant.serializers import (
    MenuSerializer,
    CategorySerializer,
    MenuItemSerializer,
)
from restaurant.models import MenuModel, CategoryModel


class TenantMenuSerializer(MenuSerializer):
    categories = CategorySerializer(many=True, read_only=True, source="category_set")

    class Meta:
        model = MenuModel
        fields = "__all__"


class TenantCategorySerializer(CategorySerializer):
    items = MenuItemSerializer(many=True, read_only=True, source="item_set")

    class Meta:
        model = CategoryModel
        fields = "__all__"
        depth = 1
