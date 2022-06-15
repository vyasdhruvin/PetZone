from django.contrib import admin
from django.urls import path
from registeration import views

urlpatterns = [
    path("Register",views.register,name="Register"),
    path("Signin",views.Signin,name='Signin'),
    path("Signout",views.Signout,name='Signout'),
]