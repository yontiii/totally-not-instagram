from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
from .forms import UserUpdateForm,ProfileUpdateForm,UserUploadForm
from django.contrib.auth.models import User
from .models import Profile,Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    images = Image.objects.all()
    users = User.objects.all()
    
    
    return render(request,'home.html',{"images":images,})
    

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
        
    
    return render(request,'users/profile.html',{"u_form":u_form})

@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        upload_form = UserUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('home.html')
        else:
            upload_form = UserUploadForm()
            
        
    
    return render(request,'uploads.html',{"upload_form":upload_form})
    