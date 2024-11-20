from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.username