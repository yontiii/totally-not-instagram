from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name='home'),
    url('^updateprofile/',views.edit_profile,name='update_profile'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url('^uploads/',views.post_image,name='post_image'),
    url('^explore/$',views.explore,name='explore'),
    url(r'^search/', views.search_results, name='search_results'),

] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    
