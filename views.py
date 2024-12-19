from django.shortcuts import render, HttpResponse, redirect
from myapp1.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    '''if request.user.is_anonymous:
        return redirect("/loginUser")'''
    #messages.success(request,"Hello!! You're Logged In !!")
    return render(request, 'index.html')
    
def about(request):
    messages.info(request, "This is about Our Website")
    return render(request, 'about.html')
 
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
        messages.success(request, 'Your meassage has been sent !')

    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def loginUser(request):
    messages.warning(request, "Hey user, Hurry Up and sign in to our website to enjoy the Shopping!!!")
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        User=authenticate(username=username, password=password)

        if User is not None:
            login(request, User)
            return redirect("/")
        else:
            return render(request, 'loginUser.html')
    return render(request,'loginUser.html')

def logoutUser(request):
    if request.method=="POST":
        logout(request)
        return render(request, 'logoutUser.html')

def SignUpUser(request):
    return render(request, 'SignUpUser.html')