from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home-page')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form =UserLoginForm(request,data=request.POST)
            if form.is_valid():
                login(request,form.get_user())
                return redirect('home-page')
        else:
            form= UserLoginForm()
        context = {
            'form':form
        }
        return render(request,'login.html',context)
    else:
        return redirect('home-page')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form =UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home-page')
        else:
            form= UserSignUpForm()
        context = {
            'form':form
        }
        return render(request,'signup.html',context)
    else:
        return redirect('home-page')