from django.db import models

# Create your models here.
class FormDetail(models.Model):
    Name       = models.TextField()
    Age        = models.DecimalField(max_digits = 150, decimal_places = 3)
    Address    = models.TextField()