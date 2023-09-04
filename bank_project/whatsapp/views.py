from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
       uname=request.POST['username']
       pasword=request.POST['password']
       user2=auth.authenticate(username=uname,password=pasword)
       if user2 is not None:
           auth.login(request,user2)
           return redirect('/')
       else:
           messages.info(request,"invalid details")
           return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        usname=request.POST['username']
        pword=request.POST['password']
        cpword=request.POST['cpassword']
        if pword==cpword:
           if User.objects.filter(username=usname).exists():
               messages.info(request,"username taken")
               return redirect('register')
           else:
               us=User.objects.create_user(username=usname,password=pword)
               us.save();
               return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def form(request):
    return render(request,"form.html")
