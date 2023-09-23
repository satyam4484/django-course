from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout
# Create your views here.

def userSignUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            userForm = UserSignUpForm(request.POST)
            profileForm =UserProfileForm(request.POST,request.FILES)
            if userForm.is_valid() and profileForm.is_valid():
                user = userForm.save()
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('login-user')
        else:
            userForm = UserSignUpForm()
            profileForm =UserProfileForm()
        context= {
            'userForm':userForm,
            'profileForm':profileForm
        }
        return render(request,'user-app/Signup.html',context)
    else:
        return redirect('home-page')



def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = userLoginForm(request,data=request.POST)
            if form.is_valid():
                login(request,form.get_user())
                return redirect('home-page')
        else:
            form = userLoginForm()
        
        context = {
            'form':form
        }
        return render(request,'user-app/login.html',context)
    else:
        return redirect('home-page')
    


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login-user')