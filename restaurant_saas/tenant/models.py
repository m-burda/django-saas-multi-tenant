from django.db import models
from django.dispatch import Signal
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase, schema_required
from tenant_users.permissions.models import UserTenantPermissions
from restaurant_saas import settings

_NameFieldLength = 64

tenant_user_added = Signal()


class Tenant(TenantBase):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    auto_drop_schema = True

    def drop_schema(self, force_drop=False):
        self._drop_schema(force_drop)

    def delete(self, *args, **kwargs):
        super(TenantMixin, self).delete(*args, **kwargs)

    def delete_and_drop_schema(self, force_drop=False, *args, **kwargs):
        """
        Deletes this row. Drops the tenant's schema if the attribute
        auto_drop_schema set to True.
        """
        self.drop_schema(force_drop)
        self.delete(self, *args, **kwargs)

    @schema_required
    def add_user(self, user_obj, is_superuser=False, is_staff=False):
        """Add user to tenant."""
        # User already is linked here..
        # if self.objects.filter(id=user_obj.id).exists():
        #     raise ExistsError(
        #         'User already added to tenant: {0}'.format(
        #             user_obj,
        #         ),
        #     )

        # User not linked to this tenant, so we need to create
        # tenant permissions
        UserTenantPermissions.objects.update_or_create(
            profile=user_obj,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        # Link user to tenant
        # user_obj.tenants.add(self)

        tenant_user_added.send(
            sender=self.__class__,
            user=user_obj,
            tenant=self,
        )

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    tenant_id = None
    tenant = models.ForeignKey(settings.TENANT_MODEL, related_name='domains',
                               on_delete=models.CASCADE, primary_key=True)
