from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name='home'),
    url('^updateprofile/',views.update_profile,name='update_profile'),
    url('^profile/',views.profile,name='profile'),
    url('^uploads/',views.post_image,name='uploads'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
