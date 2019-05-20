from django import forms
from django.contrib.auth.models import User
from .models import Profile,Image,Comments


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','website','phone_number']
        
class UserUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_caption']
        
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        field = ['comments']