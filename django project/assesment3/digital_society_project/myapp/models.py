from django.db import models

# Create your models here.

from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    

class DigitalSociety(models.Model):
    society_id = models.AutoField(primary_key=True)
    society_name = models.CharField(max_length=100)