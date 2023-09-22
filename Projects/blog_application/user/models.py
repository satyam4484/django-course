from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):  #  1 -- 1
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=11)
    gender=models.CharField(max_length=8)
    date_of_birth=models.DateField()
    profile_pic = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user


