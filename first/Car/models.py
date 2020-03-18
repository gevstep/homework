from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.IntegerField(max_length=4)
    price = models.CharField(max_length=20)
    mark = models.CharField(max_length=40)
    owner_name = models.CharField(max_length=40)
    horse_power = models.IntegerField(max_length=4)
    number_of_doors = models.IntegerField(max_length=1)
