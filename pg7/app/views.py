from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# app -> templates -> home.html

def home(request):
    age=None

    if request.method =="POST":
        age = int(request.POST.get('age'))

    context = {
        'age':age
    }

    # if age:
    #     if age >= 18:
    #         print('You are and adult')
    #     elif age >=13:
    #         print('teeager')
    #     else:
    #         print('child')

    return render(request,'home.html',context)
