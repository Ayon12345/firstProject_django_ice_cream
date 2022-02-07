from django.contrib import admin
from django.urls import path
from playground import views

urlpatterns = [
    path("", views.index, name='playground'),
    path("contact", views.contact, name='contact'),
    path("home", views.home, name='home'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),



]
