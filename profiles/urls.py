from django.contrib import admin
from django.urls import path
from profiles import views
from .views import ProfileListView,ProfileDetailView # , follow_unfollow_profile


app_name='profiles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('profileview/', views.my_profile_view, name='profileView'),
    path('profileview/', views.my_profile_api, name='profileView'),
    path('profileviewapi/', views.myprofile_apimethod, name='profileViewApi'),
    path('profileupdateapi/', views.update_profileApi, name='profileUpdateApi'),
    
    path('profilelistview/', ProfileListView.as_view(), name='profilelistview'),
    # path('hh/<pk>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('hh/<pk>/', views.ProfileDetailView, name='profile-detail-view'),
    # path('switchfollow', views.follow_unfollow_profile, name='follow_unfollow_view'),
    path('profiletlist/<int:pk>/', views.profile_list, name='profilelist'),
    path('fetch/', views.fetch, name='fetch'),
    path('postapicall/', views.post, name='post'),
    path('postapi/', views.postapi, name='post-api'),
    path('detailapi/', views.DetailProfileApi, name='detail-api'),
    ]
