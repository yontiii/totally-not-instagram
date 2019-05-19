from django.db import models
from django.contrib.auth.models  import User
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profiles/')
    bio = models.TextField(max_length=500)
    website = models.CharField(max_length=10, blank=True)
    followers = models.ManyToManyField('Profile',blank=True, related_name='followers_profile')
    following = models.ManyToManyField('Profile',blank=True,related_name='following_profile')
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.bio

class Image(models.Model):
    profile = models.ForeignKey(Profile,null=True, blank=True) 
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id):
        images = cls.objects.filter(id=id).update(id=id)
        return images
    
    def __str__(self):
        return self.image_name
    

class Comment(models.Model):
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User)
    comment = models.TextField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
