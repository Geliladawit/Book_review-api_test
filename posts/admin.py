from django.contrib import admin
from .models import Post#, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'total_likes')


admin.site.register(Post)
# admin.site.register(Comment)
