from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def otpverification(request):
    return render(request,'otpverification.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')