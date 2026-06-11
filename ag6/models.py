
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employees = models.IntegerField()

    def __str__(self):
        return self.name
# Create your models here.
