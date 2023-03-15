from restaurant.serializers import MenuSerializer, CategorySerializer
from restaurant.models import MenuModel
from rest_framework.serializers import IntegerField


class TenantMenuSerializer(MenuSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = MenuModel
        fields = ['categories',]
