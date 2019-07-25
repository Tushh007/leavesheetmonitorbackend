from django.db import models
from datetime import datetime


# Create your models here.
class Tickets(models.Model):
    checked = models.BooleanField(default="False")
    psa_id = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    user_query = models.CharField(max_length=132)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.psa_id

    class Meta:
        verbose_name_plural = "Tickets"

    class ConvertingDateTimeField(models.DateTimeField):

        def get_prep_value(self, value):
            return str(datetime.strptime(value, '%m/%d/%Y %H:%M'))
