from django.db import models

# Create your models here.
class Bookmodel(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)