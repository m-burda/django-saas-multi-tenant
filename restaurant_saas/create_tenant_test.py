import django

django.setup()

from tenant.models import Client, Domain


# create your public tenant
tenant = Client(schema_name='public',
                name='My Public Tenant',
                paid_until='2014-12-05',
                on_trial=True)
tenant.save()

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'localhost'
domain.tenant = tenant
domain.is_primary = True
domain.save()
