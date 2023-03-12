from django.db import models
from tenant_users.tenants.models import UserProfile
from django.utils.translation import gettext_lazy as _
from restaurant_saas import settings

_NameFieldLength = 64


class TenantUser(UserProfile):
    name = models.CharField(max_length=_NameFieldLength, blank=True, )
    tenants = None
