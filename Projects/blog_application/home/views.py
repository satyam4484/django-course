from django.shortcuts import render
from user.models import UserProfile

# Create your views here.


def homepage(request):
    profile = UserProfile.objects.get(user=request.user)
    context= {
        'profile':profile
    }
    return render(request,'base.html',context)