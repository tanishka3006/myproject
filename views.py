from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
   return render(request,'homepage.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    password2=request.POST['password2']
    return render(request,'postreg.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request,'dashboard.html' )

def resources(request):
    return render(request,'resources.html')
