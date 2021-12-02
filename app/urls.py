from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.abot, name='web'),
    # path('', views.webpage, name='web'),
    path('about/', views.abot, name='about'),
    path('login/', views.loginUser, name='login'),
    path('logoutuser/', views.logoutUser, name='logout'),
    path('admin/', admin.site.urls),
    
    ]
