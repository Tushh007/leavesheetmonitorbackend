from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Holidays


class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = ('date', 'day', 'holiday')
