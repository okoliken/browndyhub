from django.shortcuts import render



def Home(request):
    return render(request,'hub/home.html')
def about(request):
    return render(request,'hub/about.html')
def cart(request):
    return render(request,'hub/cart.html')

def clothe(request):
    return render(request,'hub/clothe.html')

def descrip(request):
    return render(request,'hub/descrip.html') 
# def index(request):
#     return render(request,'hub/index.html')

 
# Create your views here.
