from django.conf import settings
from django.db import models
class Casa(models.Model):
    'Generated Model'
    space = models.BigIntegerField()
class Puertas(models.Model):
    'Generated Model'
    cantidad = models.IntegerField()
