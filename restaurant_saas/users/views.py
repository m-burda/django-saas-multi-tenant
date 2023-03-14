from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer, UserRegistrationSerializer
from .models import TenantUser


class RetrieveUserModelAPIView(RetrieveAPIView):
    # queryset = TenantUser.objects.get(id=pk)
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'


class UserListAPIView(ListAPIView):
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class CreateUserAPIView(CreateAPIView):
    permission_classes = [AllowAny]

    queryset = TenantUser.objects.all()
    serializer_class = UserRegistrationSerializer


