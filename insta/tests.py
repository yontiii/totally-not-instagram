from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestCase(TestCase):
    
    # SetUp method
    def setUp(self):
        
        #creating a user instance
        self.user = User(username="john",email="k@gmail.com",password="john01")
        self.user.save()
        
        #creating a followers instance
        self.followers= 
        
        self.image = Image(user="John",profile_photo="default.jpg",bio="its me",website="www.me.com",followers="profile",)
        
