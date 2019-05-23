from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestCase(TestCase):
    
    # SetUp method
    def setUp(self):
        
        #creating a user instance
        self.user = User(username="john",email="k@gmail.com",password="john01")
        self.image = Profile(user=self.user,profile_photo="default.jpg",bio="its me",website="www.me.com")

        def tearDown(self):
            User.objects.all().delete()
            Image.objects.all().delete()
            
        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))
            
    def test_save_profile(self):
        new_user = User(id=1,username="john",email="k@gmail.com",password="john01")
        new_user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>=1)
        
    def test_delete_profile(self):
        new_user = User(id=1,username="john",email="k@gmail.com",password="john01")
        new_user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)<=0)
        
        
        
class ImageTestCase(TestCase):
    
    # SetUp method
    def setUp(self):
        
        #creating a user instance
        self.user = User(username="john",email="k@gmail.com",password="john01")
        self.image = Image(image="default.jpg",image_name="its me",image_caption="I am a good boy",date_posted="2017-8-12")

        def tearDown(self):
            User.objects.all().delete()
            Image.objects.all().delete()
            
        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))
            
    def test_save_image(self):
        new_image =Image(image="default.jpg",image_name="its me",image_caption="I am a good boy",date_posted="2017-8-12")
        new_image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>=1)
        
    def test_delete_image(self):
       new_image =Image(image="default.jpg",image_name="its me",image_caption="I am a good boy", date_posted="2017-8-12")
       new_image.delete()
       images = Image.objects.all()
       self.assertTrue(len(images)<1)
        
    
            
    
        
        
        
            
        
        
        
