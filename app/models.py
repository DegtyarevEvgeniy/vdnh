from django.db import models

class Place(models.Model):
    coordinates = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    placetype = models.CharField(max_length=100)

