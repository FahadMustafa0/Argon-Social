
from django.urls import path
from .views import PostListView, post_of_following_profiles
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('pofp/', PostListView.as_view(), name='post_list_view'),
    path('create/', views.post_create_view),
    path('', views.post_of_following_profiles, name='posts-follow-view')
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media URLs importing from settings
