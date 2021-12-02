from datetime import datetime
from django.shortcuts import render,HttpResponse ,redirect
from django.http import HttpRequest
# from app.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

def home(request):
    return render(request,'index1.html')


def abot(request):
     context={
    'variable' : "fahad"}   
     return render(request,'abot.html',context)

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,'User Not found')
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

