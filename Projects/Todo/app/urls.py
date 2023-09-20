from django.urls import path 
from .views import *

urlpatterns = [
    path('task',addTask,name='add-task'),
    path('task/delete/<int:id>',deleteTask,name='delete-task')

]
