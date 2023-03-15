from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserRegistrationSerializer
from .models import TenantUser


class RetrieveUserModelAPIView(RetrieveAPIView):
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class CreateUserAPIView(CreateAPIView):
    permission_classes = [AllowAny]

    queryset = TenantUser.objects.all()
    serializer_class = UserRegistrationSerializer
