from django.db import models

# Create your models here.

from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    # Add more fields as needed

class DigitalSociety(models.Model):
    society_id = models.AutoField(primary_key=True)
    society_name = models.CharField(max_length=100)