from django.contrib import admin

# from . import models
# # models.Student

from .models import *

# Previous way of registering models


# admin.site.register(Student)
# admin.site.register(Task)


# customization

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','age','gender']
    list_filter=['name','email']
    search_fields=['age']
