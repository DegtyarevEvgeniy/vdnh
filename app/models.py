from django.db import models

class Place(models.Model):
    coordinates = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    placetype = models.CharField(max_length=100)

class History(models.Model):
    points = models.CharField(max_length=1000)
    time = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)