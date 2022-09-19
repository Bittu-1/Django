from re import M
from unicodedata import name
from django.db import models
from django.forms import ModelChoiceField

# Create your models here.


class Customer(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    mobileno = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    salary = models.IntegerField()
    designation = models.CharField(max_length=40)

    def __str__(self):
        return self.name
