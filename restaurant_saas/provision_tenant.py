import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

from django.db.utils import IntegrityError
from users.models import TenantUser
from tenant_users.tenants.tasks import provision_tenant

user = TenantUser.objects.create_user(email="user@goodcorp.com", password='password', is_active=True)

try:
    fqdn = provision_tenant(tenant_name="Provision Test Tenant", tenant_slug="provisiontnt2", user_email="user@goodcorp.com")
except django.db.utils.IntegrityError:
    raise Exception("User may have one and only one restaurant")
