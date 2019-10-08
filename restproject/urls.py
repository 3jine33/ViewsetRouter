import post.urls
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from post import views
from userpost import views 
from rest_framework import urls 
from rest_framework.authtoken.views import obtain_auth_token # 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')), 
    path('userpost/', include('userpost.urls')), 
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]