from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('students',getStudentsList,name='student-list'),
    path('students/create',createStudentRecord,name='create-student'),
    path('students/update/<int:id>',updateStudentRecord,name='update-student'),
    path('students/delete/<int:id>',deleteStudentRecord,name='delete-student')
]
