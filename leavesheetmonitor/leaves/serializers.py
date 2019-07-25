from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Leaves


class LeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ('psa_id', 'date', 'day', 'holiday_type')
