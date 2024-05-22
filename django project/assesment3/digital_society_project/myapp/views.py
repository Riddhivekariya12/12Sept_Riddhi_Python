from django.shortcuts import render,redirect
from .models import UserProfile


# Create your views here.

def index(request):
    return render(request, 'digital_society/index.html')

def register(request):
    return render(request, 'digital_society/register.html')

def login(request):
    return render (request,'login.html')

def logout(request):
    return render(request,'logout.html')

def profile(request):
    return render(request,'profile.html')

