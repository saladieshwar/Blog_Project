from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import blogpage,nusers
# Create your views here.
def demo(request):
    return render(request,'demo.html')

@login_required(login_url='login')
def home(request):
    blogs = blogpage.objects.all()
    return render(request,'home.html',{'bloger':blogs})

def create_user(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        password = request.POST.get('password')
        user_create = User.objects.create_user(username=name, email=email, password=password)
        user_create.save()
        return redirect('login')
    return render(request,'registration.html')

def create_blogs(request):
    if request.method=='POST':
        title = request.POST.get('title')
        Author = request.POST.get('Author')
        date_time = request.POST.get('date_time')
        content = request.POST.get('content')
        bloging = blogpage(title=title, Author=Author, date_time=date_time, content=content)
        bloging.save()
        return redirect('home')
    return render(request,'blog.html')
    


def login_user(request):
    if request.method=='POST':
        name = request.POST.get('name')    
        password = request.POST.get('password')    
        login_users = authenticate(username=name, password=password)
        if login_users is not None:
            login(request,login_users)
            return redirect('home')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('demo')