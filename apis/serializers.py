from rest_framework import serializers
from posts.models import Post
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ("title", "author")
