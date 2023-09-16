from django.shortcuts import render
from records.models import Student,Teacher

# Create your views here.

def homePage(request):
    # print("i am in home function")
    studentsList = Student.objects.all() 
    teachersList = Teacher.objects.all()

    context={
        'students':studentsList,
        'teachers':teachersList
    }

    return render(request,'home.html',context)