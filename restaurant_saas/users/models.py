from django.db import models
from django.conf import settings
from tenant_users.tenants.models import UserProfile
from django.utils.translation import gettext_lazy as _


class TenantUser(UserProfile):
    name = models.CharField(max_length=64, blank=True)
    tenants = None
