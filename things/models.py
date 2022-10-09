from django.core.validators import RegexValidator
from django.db import models

class Thing():
    name =models.CharField(max_length=15)
    description=models.CharField()
    quantity = models.IntegerField()
