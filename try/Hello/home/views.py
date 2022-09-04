from email import message
from shutil import unregister_unpack_format
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    # return HttpResponse("This is Home Page")

def shop(request):
    return render(request,'shop.html')
    # return HttpResponse("This is About Page")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password =request.POST.get('password')

       
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request ,user)
            return redirect("/")
    # A backend authenticated the credentials
        else:
            return render(request,'login.html')
    # No backend authenticated the credentials

    return render(request,'login.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name = name,email = email,subject = subject,message = message ,date = datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')

    
    return render(request,'contact.html')
    # return HttpResponse("This is contact Page")


    
