import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

from tenant_users.tenants.tasks import provision_tenant

fqdn = provision_tenant(tenant_name="EvilCorp", tenant_slug="evilcorp", user_email="admin@evilcorp.com")
