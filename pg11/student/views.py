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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
        # data = request.POST
        newstudent = Student(
            name=name,
            email=email,
            contact=contact,
            age=age,
            gender=gender
        )
        newstudent.save()
        return redirect('student-list')   
    else:
        form =StudentForm()

    context={
        'form':form,
        # 'taskform':taskForm()
    }
    return render(request,'create.html',context)


def updateStudentRecord(request,id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.email =form.cleaned_data['email']
            student.contact =form.cleaned_data['contact']
            student.age =form.cleaned_data['age']
            student.gender =form.cleaned_data['gender']
            student.save()
        return redirect('student-list')   
    else:

        form = StudentForm(initial={
            'name':student.name,
            'email':student.email,
            'contact':student.contact,
            'age':student.age,
            'gender':student.gender
        })

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
