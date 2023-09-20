
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home-page'),
    path('signup',signup,name='signup-page'),
    path('login',userLogin,name='login-page'),
    path('logout',userLogout,name='userlogout')
]
