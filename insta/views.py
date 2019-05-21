from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
from .forms import UserUpdateForm,ProfileUpdateForm,UserUploadForm
from django.contrib.auth.models import User
from .models import Profile,Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    images = Image.get_all_images()
    users = User.objects.all()
    
    
    return render(request,'home.html',{"images":images,})
    

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
        
    
    return render(request,'users/update_profile.html',{"u_form":u_form})

@login_required(login_url='/accounts/login/')
def post_image(request):
    if request.method == 'POST':
        upload_form = UserUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload_form.save()
            return redirect('home.html')
    else:
        upload_form = UserUploadForm()
            
    return render(request,'uploads.html',{"upload_form":upload_form,})


@login_required(login_url='/accounts/login/')
def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    
    return render(request, 'users/profile.html',{"profile":profile,"profile_details":profile_details,"images":images})