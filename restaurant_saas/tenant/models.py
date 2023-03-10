from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | Until {self.paid_until} {"(Trial)" if {self.on_trial} else None}'


class Domain(DomainMixin):
    pass
