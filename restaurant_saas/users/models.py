from django.db import models
from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    name = models.CharField(max_length=64, blank=True)
    tenants = None
