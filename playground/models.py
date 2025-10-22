from django.db import models

class Playground(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.FloatField()
    equipment = models.TextField()
    inventory = models.IntegerField()
    description = models.TextField()
    