from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student

# Create your views here.

def createStudentRecord (request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        print(name,email,contact,age,gender)

        student = Student(name=name,email=email,contact=contact,age=age,gender=gender)
        student.save()

        return HttpResponseRedirect('/')
    
    return render(request,'student.html')

