from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author', 'genre']  
        labels = {
            'title': 'Book Title:',
            'content': 'Review:',
            'image': 'Image:'
        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
