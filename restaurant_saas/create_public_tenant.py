import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

# Create public tenant user.
from tenant_users.tenants.utils import create_public_tenant
create_public_tenant(domain_url="localhost", owner_email="admin@evilcorp.com")
