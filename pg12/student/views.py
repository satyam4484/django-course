from django.shortcuts import render,redirect
from .models import *
from .forms import *


def getStudentsList(request):
    students = Student.objects.all()

    context={
        'student_list':students,
    }
    return render(request,'home.html',context)


def createStudentRecord(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')   
    else:
        form =StudentForm()

    context={
        'form':form,
    }
    return render(request,'create.html',context)


def updateStudentRecord(request,id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')   
    else:
        form = StudentForm(instance=student)

    context={
        'student':student,
        'form':form
    }        
    return render(request,'update.html',context)



def deleteStudentRecord(request,id):
    if id:
         student = Student.objects.get(id=id)
         student.delete()
    return redirect('student-list')


'''

urls
models
templates
views
modelforms


'''