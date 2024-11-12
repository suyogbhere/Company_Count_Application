from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files')    


class Company_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.IntegerField()
    locality = models.CharField(max_length=255)
    country_linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()


