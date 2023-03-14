from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from tenant_users.tenants.tasks import provision_tenant

from .models import MenuModel, CategoryModel, MenuItemModel
from tenant.models import Tenant
from users.models import TenantUser
from tenant.serializers import TenantSerializer
from .serializers import MenuSerializer, CategorySerializer, MenuItemSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    lookup_field = "owner_id"

    # permission_classes = []

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #
    #     menus = MenuModel.objects.filter(restaurant_id=instance.owner_id)
    #     menu_serializer = MenuSerializer
    #     return Response({"restaurant": serializer.data,
    #                      "menus": [menu_serializer(menu).data for menu in menus]})

    def create(self, request, *args, **kwargs):
        data = request.POST
        email = TenantUser.objects.get(id=data['owner']).email
        try:
            provision_tenant(tenant_name=data['name'], tenant_slug=data['slug'],
                             user_email=email)
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'This user already has a restaurant.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            tenant_for_deletion = Tenant.objects.get(owner_id=kwargs['owner_id'])
            if tenant_for_deletion:
                Tenant.delete(tenant_for_deletion, force_drop=True)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except APIException:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # @action(methods=['GET'], detail=True)
    # def menu(self, **kwargs):
    #     menus = MenuModel.objects.filter(restaurant_id=kwargs['owner_id'])
    #     return Response({'menus': [MenuSerializer(menu).data for menu in menus]})


class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    # lookup_field = 'restaurant_id'

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     restaurant_id = kwargs['restaurant_owner_id']
    #     serializer = MenuSerializer(name=request.POST['name'], restaurant_id=restaurant_id)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer
    #     serializer.save()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    # def create(self, request, *args, **kwargs):
    #     print(kwargs)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer



