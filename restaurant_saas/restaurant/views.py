from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from tenant_users.tenants.tasks import provision_tenant
from django_tenants.utils import schema_exists, schema_context

from tenant.models import Tenant
from users.models import TenantUser
from tenant.serializers import TenantSerializer
from .models import MenuModel, CategoryModel, MenuItemModel
from .serializers import MenuSerializer, CategorySerializer, MenuItemSerializer


class BasicModelViewSet(viewsets.ModelViewSet):
    lookup_field = "id"

    def use_tenant_schema(func):
        lookup_value = "restaurant_owner_id"

        def wrapper(self, *args, **kwargs):
            filter_params = {"owner_id": self.kwargs[lookup_value]}
            schema_name = Tenant.objects.filter(**filter_params).values()[0][
                "schema_name"
            ]
            if schema_exists(schema_name):
                with schema_context(schema_name):
                    return func(self, *args, **kwargs)

        return wrapper

    @use_tenant_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @use_tenant_schema
    def get_object(self):
        return super().get_object()

    @use_tenant_schema
    def perform_destroy(self, instance):
        instance.delete()

    @use_tenant_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, *kwargs)

    @use_tenant_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    lookup_field = "owner_id"

    def create(self, request, *args, **kwargs):
        data = request.POST
        email = TenantUser.objects.get(id=data["owner"]).email
        try:
            provision_tenant(
                tenant_name=data["name"], tenant_slug=data["slug"], user_email=email
            )
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(
                {"error": "This user already has a restaurant."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            tenant_for_deletion = Tenant.objects.get(owner_id=kwargs["owner_id"])
            if tenant_for_deletion:
                schema_name = Tenant.objects.filter(
                    owner_id=self.kwargs["owner_id"]
                ).values()[0]["schema_name"]
                if schema_exists(schema_name):
                    with schema_context(schema_name):
                        Tenant.delete(tenant_for_deletion)
                    return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except APIException:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MenuViewSet(BasicModelViewSet):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get("restaurant_owner_id")
        if restaurant_id is not None:
            return MenuModel.objects.filter(restaurant_id=restaurant_id)


class CategoryViewSet(BasicModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        menu_id = self.kwargs.get("menu_id")
        if menu_id is not None:
            return CategoryModel.objects.filter(menu_id=menu_id)

    def perform_create(self, serializer):
        menu = self.kwargs.get("menu_id")
        serializer.save(menu_id=menu)


class MenuItemViewSet(BasicModelViewSet):
    queryset = MenuItemModel.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = "id"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return MenuItemModel.objects.filter(category_id=category_id)

    def perform_create(self, serializer):
        menu = self.kwargs.get("category_id")
        serializer.save(category_id=menu)
