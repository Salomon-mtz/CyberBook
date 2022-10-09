from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from django.template import loader 
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   
from django.views import generic
from django.views.generic import DetailView
from random import randint
import smtplib
from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import viewsets
from . serializers import EquiposSerializer, EspacioSerializer, ReservaSerializer, SoftwareSerializer
from . models import Espacios, Softwares, Reservas, Equipos
from .models import Espacios
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ast import Delete
from email import header
from email.mime.text import MIMEText
from queue import Empty
import json
from .forms import UserUpdateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required
import datetime
import sqlite3
from rest_framework import viewsets
import smtplib

codigo = ""

def index(request):
    template = loader.get_template('cyber/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=pwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Logged succesfull for: {user.username}")
            return redirect('index')
        else:
            messages.success(request, ('Bad login'))
            return render(request, 'cyber/login.html', {})
            
    else:
        return render(request, 'cyber/login.html', {})

def send_email(email, codigo):
    context = {'email':email, 'codigo':codigo}
    template = get_template('cyber/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Correo de verificación',
        'Codigo de verificación',
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.attach_alternative(content, 'text/html')
    email.send(email)

@csrf_exempt
def verificaEmail(request):
    if request.method == 'GET':
        global codigo
        codigo = str(randint(1000, 6000))
        send_email(request.user.email, codigo)
    if request.method == 'POST':
        code = request.POST['code']
        if code is not "":
            if code == codigo:

                messages.error(request, ('Registro exitoso'))
                return redirect('index')
            else:
                deleteUserEmail(request)
                messages.error(request, ('Error en codigo inteta de nuevo'))
                return redirect('index')
        else:
            messages.error(request, ('Ingresa un codigo'))
            return render(request, 'cyber/verificaEmail.html')
    else:
        return render(request, 'cyber/verificaEmail.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        username = request.POST['username']
        pwd = request.POST['password1']
        email = request.POST["email"]
        if User.objects.filter(email=email).exists():
            messages.success(request, ('correo ya registrado'))
            print(form.errors)
            return render(request, 'cyber/signup.html', {'form': form})
        else:
            if form.is_valid():
                user = form.save()
                user = authenticate(request, username=username, password=pwd, email=email)
                login(request, user)
                messages.success(request, ('Registro éxitoso'))
                return redirect("verificaEmail")
            else:
                messages.error(request, "Registro fallido")
                print(form.errors)
                return render(request, 'cyber/signup.html', {'form': form})
    else:
        return render(request, 'cyber/signup.html', {})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')

@login_required
def reservas(request, *args, **kwargs):
    espacios2 = Espacios.objects.all()
    softwares = Softwares.objects.all()
    equipos = Equipos.objects.all()
    ctx = {'espacios': espacios2, 'softwares':softwares, 'equipos':equipos}
    return render(request, 'cyber/reservas.html', ctx)

class EspaciosViewSet(viewsets.ModelViewSet):
    queryset = Espacios.objects.all().order_by('id')
    serializer_class = EspacioSerializer    
    
class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all().order_by('id')
    serializer_class = SoftwareSerializer  

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all().order_by('id')
    serializer_class = ReservaSerializer  

class EquiposViewSet(viewsets.ModelViewSet):
    queryset = Equipos.objects.all().order_by('id')
    serializer_class = EquiposSerializer  

def espacios(request, espacios_id):
    espacios = Espacios.objects.get(pk=espacios_id)
    if espacios is not None:
        return render(request, 'cyber/reservas.html', {'espacios':espacios})
    else:
        raise Http404('Imagen no existe')

def software(request, software_id):
    softwares = Softwares.objects.get(pk=software_id)
    if softwares is not None:
        return render(request, 'cyber/reservas.html', {'softwares':softwares})
    else:
        raise Http404('Imagen no existe')

def equipos(request, equipos_id):
    equipos = Equipos.objects.get(pk=equipos_id)
    if equipos is not None:
        return render(request, 'cyber/reservas.html', {'equipos':equipos})
    else:
        raise Http404('Imagen no existe')

def reservaEsp(request, espacio_id, *args, **kwargs):
    espacios = Espacios.objects.get(pk=espacio_id)
    ctx = {'espacios': espacios}
    return render(request, 'cyber/reservaEsp.html', ctx)

def reservaSoft(request, software_id, *args, **kwargs):
    softwares = Softwares.objects.get(pk=software_id)
    ctx = {'softwares': softwares}
    return render(request, 'cyber/reservaSoft.html', ctx)

def reservaEq(request, equipo_id, *args, **kwargs):
    equipos = Equipos.objects.get(pk=equipo_id)
    ctx = {'equipos': equipos}
    return render(request, 'cyber/reservaEq.html', ctx)

def profile(request):
    reservas = Reservas.objects.filter(user_id = request.user)
    ctx = {'reservas': reservas}
    return render(request, 'cyber/profile.html', ctx)

def deleteUserEmail(request):
    request.user.delete()
    return redirect('login')

def deleteUser(request):
    request.user.delete()
    messages.success(request, "Cuenta eliminada")
    return redirect('login')


def edit_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST["email"]
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if User.objects.filter(email=email).exists():
            messages.success(request, ('correo ya registrado'))
            print(u_form.errors)
            return render(request, 'cyber/edit_profile.html', {'u_form': u_form})
        else:
            if u_form.is_valid():
                print("Entra")
                u_form.save()
                return redirect('profile')
    else:
        messages.error(request, "Registro fallido")
        u_form = UserUpdateForm(instance=request.user)

    ctx = {
        'u_form': u_form,
    }
    return render(request, 'cyber/edit_profile.html', ctx)

