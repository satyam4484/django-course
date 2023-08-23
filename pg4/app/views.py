from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# app -> templates -> home.html

def home(request):
    # return HttpResponse('home') #value should a string
    context = {
        'title':'Home page',
        'desciption':'Hello this is my home page'
    }

    return render(request,'home.html',context)

def about(request):
    context = {
        'title':'about page',
        'desciption':'Hello this is my about page',
        'user':{
            'name':{
                'first_name':'satyam',
                'middle_name':'Dinesh',
                'last_name':'singh'
            },
            'email':'satyambsingh93@gmail.com',
            'contact':9106643997
        }
        # {{title}}
    }
    # nested html path
    return render(request,'user/about.html',context)
    
def contact(request):
    context = {
        'title':'contact page',
        'desciption':'Hello this is my contact page'
    }

    return render(request,'contact.html',context)
'''
root -> 3 
root -> 1 -> 4
'''