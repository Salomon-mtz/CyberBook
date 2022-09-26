from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pyrebase import pyrebase


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
    # Get a reference to the auth service
    auth = firebase.auth()
    # Log the user in
    user = auth.sign_in_with_email_and_password(email, password)
    # Get a reference to the database service
    db = firebase.database()
    # data to save
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    # Pass the user's idToken to the push method
    results = db.child("users").push(data, user['idToken'])
    template = loader.get_template('cyber/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('cyber/signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacto(request):
    template = loader.get_template('cyber/contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))
