import email
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.fname = fname
        myuser.lname = lname

        myuser.save()

        messages.success(request,"Your account has been sucessfully created")
 
        return redirect('Signin')

    return render(request,'register.html')

def Signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"products.html",{'fname':fname})
        
        else:
            messages.error(request,"Bad Credentials")
            

    return render(request,'signin.html')

def Signout(request):
    pass