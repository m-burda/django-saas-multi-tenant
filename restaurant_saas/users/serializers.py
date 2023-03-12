from rest_framework import serializers
from .models import TenantUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = [
            'email',
            'tenants',
            'is_active',
        ]
