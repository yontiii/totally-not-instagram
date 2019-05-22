from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
from .forms import UserUpdateForm,ProfileUpdateForm,UserUploadForm
from django.contrib.auth.models import User
from .models import Profile,Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    images = Image.objects.filter()
    users = User.objects.all()
    
    
    return render(request,'home.html',{"images":images,})
    

@login_required(login_url='/accounts/login')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = current_user
            form.save()
        return redirect('profile.html')
    else:
        form = ProfileUpdateForm()

    return render(request, 'users/update_profile.html', {'form':form})

@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        upload_form = UserUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            home = upload_form.save(commit=False)
            home.profile =current_user
            upload_form.save()
        return redirect('home')
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

@login_required(login_url='/accounts/login/')
def explore(request):
    images = Image.objects.all()
    
    return render(request, 'explore.html',{"images":images,} )


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'users' in request.GET and request.GET['users']:
        search_term = request.GET.get("users")
        searched_users = Profile.search_by_users(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"users":searched_users})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"users":searched_users})
        