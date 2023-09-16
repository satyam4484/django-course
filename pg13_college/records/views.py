from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.


def create_teacher(request):
    if request.method == "POST":
        form =TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=TeacherForm()
    
    context={
        'form':form
    }

    return render(request,'teachers/create_teacher.html',context)

def update_teacher(request,id):
    teacher = Teacher.objects.get(pk=id)

    if request.method == "POST":
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm(instance=teacher)
    
    context={
        'form':form,
        'teacher':teacher
    }

    return render(request,'teachers/update_teacher.html',context)

def delete_teacher(request,id):
    # print("i am in delete function")
    if id:
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
    return redirect('home')



# students


def create_student(request):
    pass

def update_student(request):
    pass

def delete_student(request):
    pass

