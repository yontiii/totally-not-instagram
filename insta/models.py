from django.db import models
from django.contrib.auth.models  import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg',upload_to='profiles/')
    bio = models.TextField(max_length=500,default='Tell Me Something')
    website = models.CharField(max_length=10, blank=True,default='me.com')
    followers = models.ManyToManyField('Profile',blank=True, related_name='followers_profile')
    following = models.ManyToManyField('Profile',blank=True,related_name='following_profile')
    phone_number = models.CharField(max_length=10,default=12345678)
    
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  
        
    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls,id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    
    
    def __str__(self):
        return self.bio

class Image(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField(max_length=150)
    date_posted = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('date_posted',)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id):
        images = cls.objects.filter(id=id).update(id=id)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
    
    @classmethod
    def get_profile_images(cls,profile):
        images = Image.objects.filter(profile__pk=profile)
        print(images)
        return images
    
    def __str__(self):
        return self.image_name
    

class Comments(models.Model):
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def save_comment(self):
        self.save()
        
    @classmethod
    def get_comments_by_images(cls , id):
        comments = Comments.objects.filter(image__pk=id)
    
    def __str__(self):
        return self.comment
    
