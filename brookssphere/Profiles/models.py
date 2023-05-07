from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=80, default="name") 
    # TODO - fix this to be MM/DD/YYYY
    date_of_birth = models.DateTimeField(default=datetime.datetime.now())
    operations_performed = models.IntegerField(default = 0)

