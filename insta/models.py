from django.db import models


class Profile(models.Model):
    profile_photo = models.ImageField(uploadto='profiles/')
    bio = models.TextField(max_length=500)

class Image(models.Model):
    image = models.ImageField(uploadto='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField(max_length=150)
    likes = models.IntegerField(max_length=20)
    comments = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile)
    
