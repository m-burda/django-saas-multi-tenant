from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer
from .models import TenantUser


class RetrieveUserModelAPIView(RetrieveAPIView):
    # queryset = TenantUser.objects.get(id=pk)
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'


@permission_classes([IsAuthenticated])
class UserListAPIView(ListAPIView):
    queryset = TenantUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
