from django.db import models
from tenant_users.tenants.models import UserProfile

_NameFieldLength = 64


class TenantUser(UserProfile):
    name = models.CharField(max_length=_NameFieldLength, blank=True)
    tenants = None
