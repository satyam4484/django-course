from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}_{self.email}'
    


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    experience=models.IntegerField()

    def __str__(self):
        return f'{self.name}_{self.email}_Teaches_{self.subject}'
    

    