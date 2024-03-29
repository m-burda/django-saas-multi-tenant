import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

from tenant_users.tenants.models import ExistsError
from tenant_users.tenants.utils import create_public_tenant

try:
    create_public_tenant(domain_url=os.environ['PUBLIC_TENANT_DOMAIN'], owner_email=os.environ['PUBLIC_TENANT_EMAIL'])
except ExistsError as err:
    print(err)
