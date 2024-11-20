from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def custom_logout_view(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect('home')  
