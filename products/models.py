from django.db import models

# Create your models here.
class Mobile(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default="This is a cool!")
    featured    = models.BooleanField()

class Fruit(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default="This is a cool!")
    featured    = models.BooleanField()

class Car(models.Model):
    title       = models.TextField(max_length=200)
    description = models.TextField(blank = True)
    price       = models.DecimalField(max_digits = 10000, decimal_places = 2)
    summary     = models.TextField(default="This is a cool!")
    featured    = models.BooleanField()    