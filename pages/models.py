from django.db import models

# Create your models here.
class Page(models.Model):
    content = models.TextField()
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self):
        return self.title