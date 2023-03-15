import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_saas.settings")
django.setup()

from django.db.utils import IntegrityError
from users.models import TenantUser
from tenant_users.tenants.tasks import provision_tenant
from django_tenants.utils import schema_exists, tenant_context


def provision_tenant_custom(email, pwd):
    user = TenantUser.objects.create_user(email="user@goodcorp.com", password='password', is_active=True)

    try:
        fqdn = provision_tenant(tenant_name="Provision Test Tenant", tenant_slug="provisiontnt2",
                                user_email="user@goodcorp.com")
    except django.db.utils.IntegrityError:
        raise Exception("User may have one and only one restaurant")


def create_user(email, pwd):
    data = {
        'email': email,
        'password': pwd,
        'password2': pwd,
    }

    requests.post('http://localhost:8000/users/register/', json=data)


create_user('user@goodcorp.com', '2222')
# provision_tenant(tenant_name="Provision Test Tenant", tenant_slug="provisiontnt2",
#                                 user_email="user@goodcorp.com")
