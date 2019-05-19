from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    return HttpResponse('Welcome to instagram')
    

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'users/profile.html')