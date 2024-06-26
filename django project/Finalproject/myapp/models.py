from django.db import models

# Create your models here.

class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class notes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='NotesFolder')
    desc=models.TextField()

class callback(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()