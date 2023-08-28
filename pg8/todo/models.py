from django.db import models
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    # attribute : models.datatype()
    task_name = models.CharField(max_length=50)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
    

