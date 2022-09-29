from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pyrebase import pyrebase

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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
    template = loader.get_template('cyber/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("cyber/index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="cyber/signup.html", context={"register_form":form})

def contacto(request):
    template = loader.get_template('cyber/contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))
