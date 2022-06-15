from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def products(request):
    return render(request,'products.html')

def Support(request):
    return render(request,'support.html')