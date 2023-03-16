from rest_framework.generics import RetrieveAPIView
from restaurant.models import MenuModel, CategoryModel, MenuItemModel
from restaurant.serializers import MenuSerializer


class TenantMenuView(RetrieveAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'
