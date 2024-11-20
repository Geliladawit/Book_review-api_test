from django.urls import path
from .views import HomePageView,  Post
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/upload', Post, name='upload'),
]
