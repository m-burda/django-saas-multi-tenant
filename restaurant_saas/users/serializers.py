from rest_framework import serializers
from .models import TenantUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = [
            'id',
            'email',
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = TenantUser
        fields = [
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def save(self):
        user = TenantUser(
            email=self.validated_data['email'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if not self.validate_pass(password,
                                  password2):
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        else:
            TenantUser.objects.create_user(email=user.email,
                                           password=password,
                                           is_active=True)
        return user

    @staticmethod
    def validate_pass(pass1, pass2):
        return pass1 == pass2
