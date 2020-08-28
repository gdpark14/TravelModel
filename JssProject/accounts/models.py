from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from main.views import Jasosel

# Create your models here.
class Profile(models.Model):
    person=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    introduction=models.TextField(blank=True)
