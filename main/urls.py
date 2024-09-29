from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('main',views.usepage,name='main'),
    path('getacoffe',views.getacoffee,name='getacoffee'),
    path('strt',views.strt),

]