from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from leavesheetmonitor.users.models import User
from leavesheetmonitor.users.serializers import UserSerializer
# Also add these imports
from leavesheetmonitor.users.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
