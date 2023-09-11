from django.shortcuts import render
from . import models


# Create your views here.
def home(request):

    tasks = models.Todo.objects.all()
    '''
        select * from todo;
    '''

    for item in tasks:
        print(item)

    if request.method == "POST":
        newTask=request.POST.get('task_name')
        if newTask:
            task = models.Todo(task_name=newTask)
            task.save()

    context = {
        'all_tasks':tasks
    }
    return render(request,'home.html',context)




