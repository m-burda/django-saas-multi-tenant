from django.db import models
from django.dispatch import Signal
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase, schema_required
from tenant_users.permissions.models import UserTenantPermissions
from restaurant_saas import settings

tenant_user_added = Signal()


class Tenant(TenantBase):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    auto_drop_schema = False

    def delete(self, force_drop=False, *args, **kwargs):
        super(TenantMixin, self).delete(force_drop, *args, **kwargs)
        super()._drop_schema(force_drop=True)

    @schema_required
    def add_user(self, user_obj, is_superuser=False, is_staff=False):
        UserTenantPermissions.objects.update_or_create(
            profile=user_obj,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

        tenant_user_added.send(
            sender=self.__class__,
            user=user_obj,
            tenant=self,
        )

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    tenant_id = None
    tenant = models.ForeignKey(
        settings.TENANT_MODEL,
        related_name="domains",
        on_delete=models.CASCADE,
        primary_key=True,
    )
