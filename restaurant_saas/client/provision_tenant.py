import os
from django.db.utils import IntegrityError
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

from tenant_users.tenants.tasks import provision_tenant

try:
    fqdn = provision_tenant(tenant_name="Provision Test Tenant", tenant_slug="provisiontnt", user_email=os.environ['PUBLIC_TENANT_EMAIL'])
except django.db.utils.IntegrityError:
    raise Exception("User may have one and only one restaurant")
