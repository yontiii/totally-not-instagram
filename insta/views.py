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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    
    return render(request,'users/profile.html',{"u_form":u_form,"p_form":p_form})