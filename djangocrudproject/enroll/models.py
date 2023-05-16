from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    misId = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    year = models.CharField(max_length=70)
    division = models.CharField(max_length=70)
    department = models.CharField(max_length=70)
    cgpa = models.CharField(max_length=70)
    attendance = models.CharField(max_length=70)
