from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from .forms import SearchForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse  
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from users.models import CustomUser

def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user  
            post.save()
            return redirect('home')
        
    else: 
        form = PostForm()

    return render(request, 'upload.html', {'form': form})

def home(request):
    search_query = request.GET.get('search', '')  
    sort_by = request.GET.get('sort', '')
    posts = Post.objects.all() 

    if search_query:
        posts = posts.filter(title__icontains=search_query)  
    if sort_by == 'most_liked':
        posts = posts.annotate(like_count=Count('likes')).order_by('-like_count', '-created_at')
    else:
        posts = posts.order_by('-created_at')
    context = {
        'posts': posts,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'home.html', context)

User = get_user_model()

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    liked = False
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user) 
    else:
        post.likes.add(user)  
        liked = True
    data = {
        'liked': liked,
        'total_likes': post.total_likes(),
    }
    return JsonResponse(data)

@login_required
def my_posts(request):
    user_posts = Post.objects.filter(created_by=request.user)
    context = {
        'posts': user_posts,
        'followers_count': request.user.followers.count(),  
        'following_count': request.user.following.count(),  
    }
    return render(request, 'my_posts.html', context)  
# Create your views here.
class PostsUpdateView(UpdateView): 
    model = Post
    fields = ('title', 'author','genre','content','image')
    template_name = 'post_edit.html'
    success_url = reverse_lazy('my_posts')

class PostsDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('my_posts')

@login_required
def follow_unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    user = request.user

    if user == target_user:
        return JsonResponse({'error': 'You cannot follow yourself'}, status=400)

    if target_user in user.following.all():
        user.following.remove(target_user)
        followed = False
    else:
        user.following.add(target_user)
        followed = True

    data = {
        'followed': followed,
        'followers_count': target_user.followers.count(),
    }
    return JsonResponse(data)

def profile(request, user_id):
    profile_user = get_object_or_404(CustomUser, id=user_id)
    context = {
        'profile_user': profile_user,
        'followers_count': profile_user.followers.count(), 
    }
    return render(request, 'home.html', context)

