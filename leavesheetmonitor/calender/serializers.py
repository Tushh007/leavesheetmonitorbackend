from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Calender


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('month', 'date', 'day', 'day_type')
