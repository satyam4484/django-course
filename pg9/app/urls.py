
from django.urls import path
# from . import views 
from .views import *


urlpatterns = [
    # path('add-student',views.createStudentRecord)

    path('add-student',createStudentRecord,name='addStudent')
]