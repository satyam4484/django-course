
from django.urls import path
from .views import *


urlpatterns = [
    # teachers
    path('teachers/create',create_teacher,name='create-teacher'),
    path('teachers/update/<int:id>',update_teacher,name='update-teacher'),
    path('teachers/delete/<int:id>',delete_teacher,name='delete-teacher'),

    # students
    path('students/create',create_student,name='create-student'),
    path('students/update/<int:id>',update_student,name='update-student'),
    path('students/delete/<int:id>',delete_student,name='delete-student'),

]



