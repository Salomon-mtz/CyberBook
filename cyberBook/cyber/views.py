from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pyrebase import pyrebase

def index(request):
    template = loader.get_template('cyber/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
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
