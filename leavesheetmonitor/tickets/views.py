from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from leavesheetmonitor.tickets.permissions import IsAdminUser
from .serializers import TicketsSerializer
from .models import Tickets
from rest_framework.response import Response


class TicketsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

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
        tickets = Tickets.objects.all()
        serializer = TicketsSerializer(tickets, many=True)
        return Response(serializer.data)
