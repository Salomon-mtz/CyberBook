from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import loader 
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   
import hashlib
from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import viewsets
from . serializers import EquiposSerializer, EspacioSerializer, ReservaSerializer, SoftwareSerializer
from . models import Espacios, Softwares, Reservas, Equipos
from .models import Espacios

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

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        username = request.POST['username']
        pwd = request.POST['password1']
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=username, password=pwd)
            login(request, user)
            messages.success(request, ('Registro éxitoso'))
            return redirect("index")
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
    queryset = Espacios.objects.all().order_by('idEsp')
    serializer_class = EspacioSerializer    
    
class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all().order_by('idSoft')
    serializer_class = SoftwareSerializer  

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all().order_by('id')
    serializer_class = ReservaSerializer  

class EquiposViewSet(viewsets.ModelViewSet):
    queryset = Equipos.objects.all().order_by('idEq')
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