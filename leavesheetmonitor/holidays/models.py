from django.db import models
# from datetime import datetime


# Create your models here.
class Holidays(models.Model):

    date = models.DateField()
    day = models.CharField(max_length=9)
    holiday = models.CharField(max_length=20)

    def __str__(self):
        return self.holiday

    class Meta:
        verbose_name_plural = "Holidays"

    # class ConvertingDateTimeField(models.DateTimeField):
        # def get_prep_value(self, value):
        #     return str(datetime.strptime(value, '%m/%d/%Y %H:%M'))
