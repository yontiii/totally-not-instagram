from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
from .forms import UserUpdateForm,ProfileUpdateForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    return HttpResponse('Welcome to instagram')
    

@login_required(login_url='/accounts/login/')
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    return render(request,'users/profile.html',{"u_form":u_form,"p_form":p_form})