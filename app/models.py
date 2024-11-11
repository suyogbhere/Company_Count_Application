from django.db import models

# Create your models here.

class Company_data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    year = models.IntegerField()
    state = models.CharField(max_length=200)


