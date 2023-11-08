from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.IntegerField()

class Authorization(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)