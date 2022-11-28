from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('anime', views.anime, name='anime'),
    path('bollywood', views.bollywood, name='bollywood'),
    path('hollywood', views.hollywood, name='hollywood'),
    path('justarrived', views.justarrived, name='justarrived'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]