from django.contrib import admin
from django.urls import path
from profiles import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profileview/', views.my_profile_view, name='profileView'),
    
    ]
