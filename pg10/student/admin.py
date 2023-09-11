from django.contrib import admin
# from . import models 
from .models import *
# Register your models here.

# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','contact','age','gender']