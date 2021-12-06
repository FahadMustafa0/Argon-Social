"""
Definition of urls for app
"""

from datetime import datetime
from django.urls import path,include 
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header="fahad app Admin"
admin.site.site_title="fahad app Admin portal"
admin.site.index_title="wellcome to my app"



urlpatterns = [
    path('', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    # path("contact", views.kontact, name='contact'),
    # path("about", views.abot, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)