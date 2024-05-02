from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'digital_society/index.html')

def register(request):
    return render(request, 'digital_society/register.html')

def index(request):
    return render (request,'index.html')

def register(request):
    return render(request,'register.html')