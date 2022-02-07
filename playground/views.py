from lib2to3.fixes.fix_input import context

import login as login
from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Login


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is a playground")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('Contact us')


def home(request):
    return render(request, 'index.html')


# return HttpResponse('This is our homepage')


def login(request):
    global login
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        login = Login(email=email, password=password)
        login.save()

    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

    # return HttpResponse('It will find your location')


def thumb(request):
    image = request.POST.get('image')
    description = request.POST.get('description')

