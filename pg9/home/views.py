from django.shortcuts import render
from app.models import *

# Create your views here.

def home(request):
    student_list = Student.objects.all()
    
    context = {
        'students':student_list
    }
    return render(request,'home.html',context)