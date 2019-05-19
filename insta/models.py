from django.db import models



class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/',default='default.jpg')
    bio = models.TextField(max_length=500)
    website = models.CharField(max_length=20, blank=True)
    followers = models.ManyToManyField('Profile',blank=True, related_name='followers_profile')
    following = models.ManyToManyField('Profile',blank=True,related_name='following_profile')
    phone_number = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.TextField(max_length=150)
    likes = models.IntegerField()
    comments = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile) 
    
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
    
