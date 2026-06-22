from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="students")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
