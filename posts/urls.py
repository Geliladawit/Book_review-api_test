from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
PostsUpdateView,
PostsDeleteView,)
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('myposts/', views.my_posts, name='my_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('<int:pk>/edit/',PostsUpdateView.as_view(), name='post_edit'), 
    path('<int:pk>/delete/', PostsDeleteView.as_view(), name='post_delete'),
    path('follow/<int:user_id>/', views.follow_unfollow_user, name='follow_unfollow_user'), 

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
