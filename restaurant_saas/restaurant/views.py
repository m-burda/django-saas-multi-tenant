from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django_tenants.models import TenantMixin
from tenant_users.tenants.tasks import provision_tenant
from django_tenants.utils import schema_exists, schema_context

from tenant.models import Tenant
from users.models import TenantUser
from tenant.serializers import TenantSerializer
from .models import MenuModel, CategoryModel, MenuItemModel
from .serializers import MenuSerializer, CategorySerializer, MenuItemSerializer


def get_schema_from_tenant(parent_model, lookup_value):
    filter_params = {f"owner_id": lookup_value}
    return parent_model.objects.filter(**filter_params).values()[0]["schema_name"]


class BasicModelViewSet(viewsets.ModelViewSet):
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        schema_name = get_schema_from_tenant(Tenant, self.kwargs["restaurant_owner_id"])
        if schema_exists(schema_name):
            with schema_context(schema_name):
                instance = self.get_object()
                serializer = self.get_serializer(
                    instance, data=request.data, partial=partial
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
            if getattr(instance, "_prefetched_objects_cache", None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)

    def get_object(self):
        schema_name = get_schema_from_tenant(Tenant, self.kwargs["restaurant_owner_id"])
        if schema_exists(schema_name):
            with schema_context(schema_name):
                return super().get_object()

    def perform_destroy(self, instance):
        schema_name = get_schema_from_tenant(Tenant, self.kwargs["restaurant_owner_id"])
        with schema_context(schema_name):
            instance.delete()

    def create(self, request, *args, **kwargs):
        schema_name = get_schema_from_tenant(Tenant, self.kwargs["restaurant_owner_id"])
        if schema_exists(schema_name):
            with schema_context(schema_name):
                return super().create(request, *args, *kwargs)

    def list(self, request, *args, **kwargs):
        schema_name = get_schema_from_tenant(Tenant, self.kwargs["restaurant_owner_id"])
        if schema_exists(schema_name):
            with schema_context(schema_name):
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
                schema_name = get_schema_from_tenant(Tenant, self.kwargs["owner_id"])
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
