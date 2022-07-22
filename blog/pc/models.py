import email
from turtle import title
from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()

class signup(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)

class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField()    
