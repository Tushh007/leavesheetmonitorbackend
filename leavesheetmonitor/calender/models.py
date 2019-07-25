from django.db import models
from datetime import datetime


# Create your models here.
class Calender(models.Model):

    month = models.CharField(max_length=20)
    date = models.DateField()
    day = models.CharField(max_length=9)
    day_type = models.CharField(max_length=20)

    def __str__(self):
        return self.date.strftime('%d/%m/%y')
