from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=6, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    psa_id = models.CharField(max_length=7)
    role = models.CharField(max_length=15, default="member")
    manager_psa_id = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=50)
    manager_email = models.EmailField(max_length=50)
