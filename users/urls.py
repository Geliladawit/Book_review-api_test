from django.urls import path
from .views import SignUpView
from . import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.custom_logout_view, name='logout'),
]