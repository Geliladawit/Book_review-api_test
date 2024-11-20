from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from posts.models import Post
from .serializers import BookSerializer
class BookAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BookSerializer
