from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tickets


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id', 'checked', 'psa_id', 'email', 'user_query', 'date')
