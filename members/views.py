from cgi import print_arguments
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html',{})
        else:
            print("Heyyy DO NOT PASS")
            return redirect('login')

    return render(request,'registration/login.html',{})


def logout_user(request):
    logout(request)
    return redirect('login')