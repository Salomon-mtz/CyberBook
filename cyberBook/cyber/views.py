from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pyrebase import pyrebase
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   
import hashlib

config = {
  "apiKey": "AIzaSyCDvxtOqMSsiQ38fgNZ8uaDIvsc2EqUr00",
  "authDomain": "cyberbook-d8b6a.firebaseapp.com",
  "databaseURL": "https://cyberbook-d8b6a-default-rtdb.firebaseio.com/",
  "storageBucket": "cyberbook-d8b6a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
def index(request):
    template = loader.get_template('cyber/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            pwd = request.POST['password1']
            
            user = authenticate(request, username=username, password=pwd)
            
            if user is not None:
                login(request, user)    
                return redirect('cyber/index.html')
                messages.success(request, ('Good login'))
            else:
                messages.error(request, ('Bad login'))
                return render(request, 'cyber/login.html', {})
            
    else:
        return render(request, 'cyber/login.html', {})

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        username = request.POST['username']
        pwd = request.POST['password1']
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=username, password=pwd)
            login(request, user)
            messages.success(request, ('Registration seccessful'))
            return redirect("cyber/index.html")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            print(form.errors)
            return render(request, 'cyber/signup.html', {'form': form})
    else:
        return render(request, 'cyber/signup.html', {})

def contacto(request):
    template = loader.get_template('cyber/contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))
