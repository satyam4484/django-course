from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UserProfile)
class userProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','contact','gender','date_of_birth','profile_pic']