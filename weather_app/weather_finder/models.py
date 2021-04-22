from django.db import models

# Create your models here.
class Cordinates(models.Model):

    lattitude = models.DecimalField(max_digits=7, decimal_places=7)
    longitude = models.DecimalField(max_digits=7, decimal_places=7)
