from django.shortcuts import render,redirect
from .models import *


def getStudentsList(request):
    students = Student.objects.all()

    context={
        'student_list':students
    }
    return render(request,'home.html',context)

def createStudentRecord(request):
    if request.method == "POST":
        data = request.POST
        newstudent = Student(name=data['name'],email=data['email'],contact=data['contact'],age=int(data['age']),gender=data['gender'])
        newstudent.save()
        return redirect('student-list')   
        
    return render(request,'create.html')


def updateStudentRecord(request,id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        student.name = data['name']
        student.email =data['email']
        student.contact =data['contact']
        student.age =data['age']
        student.gender =data['gender']
        student.save()

        return redirect('student-list')   

    context={
        'student':student,
    }        
    return render(request,'update.html',context)

def deleteStudentRecord(request,id):
    if id:
         student = Student.objects.get(id=id)
         student.delete()
    return redirect('student-list')
