from rest_framework.generics import RetrieveAPIView
from restaurant.models import MenuModel, CategoryModel, MenuItemModel
from restaurant.serializers import MenuSerializer, CategorySerializer, MenuItemSerializer
from .serializers import TenantMenuSerializer, TenantCategorySerializer


class TenantMenuView(RetrieveAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = TenantMenuSerializer
    lookup_field = 'id'


class TenantCategoryView(RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = TenantCategorySerializer
    lookup_field = 'id'


class TenantItemView(RetrieveAPIView):
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'

    # def get_queryset(self):
    #     menu_id = self.kwargs['id']
    #     return MenuModel.objects.filter(id=menu_id)


# class TenantCategoryView(RetrieveAPIView):
#     queryset = CategoryModel.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'id'
#
#
# class TenantMenuItemView(RetrieveAPIView):
#     queryset = MenuItemModel.objects.all()
#     serializer_class = MenuItemSerializer
#     lookup_field = 'id'
