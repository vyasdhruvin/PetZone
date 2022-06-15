from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
       path('admin/',admin.site.urls),
       path("",views.home,name='home'),
       path("home",views.home,name='home'),
       path("about",views.about,name='about'),
       path("products",views.products,name='products'),
       path("Support",views.Support,name='Support')
]
