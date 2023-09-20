from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from .forms import TaskForm
# Create your views here.


def addTask(request):
    if request.method== "POST":
        form= TaskForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            userform.user = request.user
            userform.save()
        return redirect('home-page')
    else:
        form =TaskForm()

    context= {
        'form':form
    }

    return render(request,'addtask.html',context)

def deleteTask(request,id):
    
    if request.user.is_authenticated and id:
        task = Task.objects.get(pk=id)
        task.delete()


    return redirect('home-page')

    # rollback ,commit 

    # DDl,DMl,DCL,TCL