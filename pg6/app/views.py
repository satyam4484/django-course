from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# app -> templates -> home.html

def home(request):
    email = None
    password= None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

    context= {
        'email':email,
        'password':password
    }
    return render(request,'home.html',context)