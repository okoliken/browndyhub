from django.shortcuts import render,redirect


def signup(request):
        return render(request,'hub/signup.html')    
# Create your views here.


def login(request):
        return render(request,'hub/login.html')

def logout(request):
    return render(request,'hub/logout.html')
