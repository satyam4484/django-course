from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField()
    contact =models.CharField(max_length=11)
    age=models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        obj = 'My name is '+ self.name + ' and my email is '+ self.email
        return obj
     