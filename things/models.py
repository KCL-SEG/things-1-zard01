from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
class Thing(AbstractUser):
    name =models.CharField(max_length=15)
    description=models.CharField()
    quantity = models.IntegerField()
