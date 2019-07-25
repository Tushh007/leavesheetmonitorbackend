from django.db import models


# Create your models here.
class Leaves(models.Model):

    psa_id = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    date = models.DateField()
    day = models.CharField(max_length=9)
    holiday_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Leaves"

