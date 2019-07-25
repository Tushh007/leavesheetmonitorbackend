from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from leavesheetmonitor.holidays.permissions import IsAdminUser
from .serializers import HolidaysSerializer
from .models import Holidays
from rest_framework.response import Response


class HolidaysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Holidays.objects.all()
    serializer_class = HolidaysSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        holidays = Holidays.objects.all()
        serializer = HolidaysSerializer(holidays, many=True)
        return Response(serializer.data)
