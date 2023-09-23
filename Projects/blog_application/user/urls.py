from django.urls import path 
from .views import *
urlpatterns = [
    path('create',userSignUp,name='sign-up'),
    path('login',userLogin,name='login-user'),
    path('logout',userLogout,name='logout-user')
]
