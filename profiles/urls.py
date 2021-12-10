from django.contrib import admin
from django.urls import path
from profiles import views
from .views import ProfileListView,ProfileDetailView,follow_unfollow_profile

app_name='profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('profileview/', views.my_profile_view, name='profileView'),
    path('profilelistview/', ProfileListView.as_view(), name='profilelistview'),
    path('hh/<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('switchfollow', views.follow_unfollow_profile, name='follow_unfollow_view'),
    ]
