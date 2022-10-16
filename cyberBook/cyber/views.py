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
from . models import Espacios, Softwares, Reservas, Equipos, Usuarios
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
from django.contrib.auth import logout, login as auth_login, authenticate
import hashlib
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
import ast
from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import viewsets
from . serializers import EquiposSerializer, EspacioSerializer, ReservaSerializer, SoftwareSerializer, UsuarioSerializer
from . models import Espacios, Softwares, Reservas, Equipos, Usuarios
from json import loads, dumps
from django.contrib.auth import authenticate, login as loginUser, logout
from ast import Delete
from email import header
from email.mime.text import MIMEText
from queue import Empty
import json
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse


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
        telefono = request.POST['phone']
        rol = request.POST['rol']
        escuela = request.POST['school']
        nombre2 = username
        if Usuarios.objects.filter(email=email).exists():
            messages.success(request, ('correo ya registrado'))
            print(form.errors)
            return render(request, 'cyber/signup.html', {'form': form})
        else:
            if form.is_valid():
                contraseña1 = hashlib.sha256(pwd.encode())
                contraseña2 = contraseña1.hexdigest()
                user2 = Usuarios.objects.create(username = nombre2, password = contraseña2, email = email, phone=telefono, school=escuela, rol=rol)
                user = form.save()
                user = authenticate(request, username=username, password=pwd, email=email)
                auth_login(request, user)
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
    query = Usuarios.objects.get(email = request.user.email)
    reservas = Reservas.objects.filter(user_id = query)
    esp = Reservas.objects.filter(user_id = query).filter(idServicio = "1").count()
    eq = Reservas.objects.filter(user_id = query).filter(idServicio = "2").count()
    soft = Reservas.objects.filter(user_id = query).filter(idServicio = "3").count()
    ctx = {'reservas': reservas,
            'esp' : esp,
            'eq' : eq,
            'soft' : soft,
            'usuario' : query
        }
    return render(request, 'cyber/profile.html', ctx)

@csrf_exempt
def deleteUserEmail(request):
    print(request.user.email)
    query = Usuarios.objects.get(email = request.user.email)
    query.delete()
    request.user.delete()
    return redirect('login')

def deleteUser(request):
    request.user.delete()
    messages.success(request, "Cuenta eliminada")
    return redirect('login')


def edit_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        telefono = request.POST['phone']
        rol = request.POST['rol']
        escuela = request.POST['school']
        password = request.POST.get('password', False)
        query = Usuarios.objects.get(email = request.user.email)
        u_form = UserUpdateForm(request.POST, instance=query)
        u = request.user
        if u_form.is_valid():
            contraseña1 = hashlib.sha256(password.encode())
            contraseña2 = contraseña1.hexdigest()
            query.password = contraseña2
            u_form.save()
            u.set_password(password)
            u.username = username
            u.save()
            u.telefono = telefono
            u.save()
            u.rol = rol
            u.save()
            u.escuela = escuela
            u.save()
            messages.success(request, ('Inicia Sesión para verificar tu nueva contraseña:'))
            return redirect('login')
        else:
            messages.error(request, "Registro fallido")
            print(u_form.errors)

    else:
        query = Usuarios.objects.get(email = request.user.email)
        u_form = UserUpdateForm(instance=query)

    ctx = {
        'u_form': u_form,
    }
    return render(request, 'cyber/edit_profile.html', ctx)

    #APP
class EspaciosViewSet(viewsets.ModelViewSet):
    queryset = Espacios.objects.all().order_by('id')
    serializer_class = EspacioSerializer    
    
class SoftwaresViewSet(viewsets.ModelViewSet):
    queryset = Softwares.objects.all().order_by('id')
    serializer_class = SoftwareSerializer  


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer  

class EquiposViewSet(viewsets.ModelViewSet):
    queryset = Equipos.objects.all().order_by('id')
    serializer_class = EquiposSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all().order_by('id')
    serializer_class = UsuarioSerializer  
    
    

@csrf_exempt
def hacerLoginApp(request):
    if request.method == 'POST':
        var = request.body
        print(var)
        dicc = ast.literal_eval(var.decode('utf-8'))
        u = Usuarios.objects.filter(email=dicc['correo']).first()
        l = list(dicc.values())
        pwd = l[0]
        pas = hashlib.sha256(pwd.encode())
        passw = pas.hexdigest()
        print(passw)
        
        print(u.password)
        if (passw == u.password):
            json = dumps({"msg": "Accesado", "id":u.id})
            return HttpResponse(json, content_type="application/json")
        else:
            json = dumps({"msg": "Inaccesible"})
            return HttpResponse(json, content_type="application/json")
    else:
        return HttpResponse("Please use POST")


@csrf_exempt
def getUsuariosApp(request):

    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    email = body["email"]
    print(email)

    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()

    getUsuarios = "SELECT email FROM cyber_usuarios WHERE cyber_usuarios.email = ?"
    rows = cur.execute(getUsuarios,(email,)).fetchall()
    print(rows)

    if not rows:
        json = dumps({"msg":"No registrado"})
    else:

        json = dumps({"msg":"registrado"})

    print(json)

    mydb.commit()
    mydb.close()

    return HttpResponse(json, content_type="application/json")

@csrf_exempt
def registrarUsuarioApp(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    name = body["name"]
    email = body["email"]
    pwd = body["password"]
    pas = hashlib.sha256(pwd.encode())
    passw = pas.hexdigest()
    phone = body["phone"]
    school = body["school"]
    rol = body["rol"]
    
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    user = cursor.execute("insert into cyber_usuarios (username, password, email, phone, rol, school) values (?, ?, ?, ?, ?, ?)",
            (name, passw, email, phone, rol, school))
    print(cursor.lastrowid)
    user_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return JsonResponse({"msg": "usuario registrado", "id":user_id})

    
@csrf_exempt
def enviarMail(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    email = body["email"]
    code = body["code"]

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "CyberBook: Codigo de verificacion"

    # message to be sent
    htmlMssg = '''
        <html>
        <head></head>
        <body>
            <h2>Codigo de activacion</h2>
            <p> Por favor introduzca el siguiente codigo dentro de la aplicacion:
            <h3><b> ''' + str(code) + '''
            </b></h3>
                 </p>
                 </body>
             </html>
                '''

    message = MIMEText(htmlMssg,'html')
    msg.attach(message)

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.starttls()

    # Authentication
    gmail.login("cyberbooktec22@gmail.com", "xakijnjmijzvvkat")
    # sending the mail
    gmail.sendmail("cyberbooktec22@gmail.com", email, msg.as_string())
    # terminating the session
    gmail.quit()


    json = dumps({"msg": "Ended process"})

    return HttpResponse(json, content_type="application/json")

@csrf_exempt
def logoutApp(req):
    print("Logout")
    print(req.user)

    logout(req)

    json = dumps({"msg": "Logged out"})
    return HttpResponse(json, content_type="application/json")

@csrf_exempt
def getReserva(request):
    userId = request.GET["user_id"]
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()

    getReserva = "SELECT * FROM cyber_reservas WHERE cyber_reservas.user_id_id = ?"
    rows = cur.execute(getReserva, (userId,)).fetchall()

    if rows is None:
        raise Http404("user_id does not exist")
    else:

        lista_salida = []
        for r in rows:
            d = {
                "id": r[0],
                "fecha": r[1],
                "tipoRes": r[2],
                "estatus": r[3],
                "tiempoRes": r[4],
                "codigo": r[5],
                "user_id": r[7],
                "idServicio": r[6]
                
            }
            lista_salida.append(d)
            print(lista_salida[0])

        json = dumps(lista_salida)
    mydb.commit()
    mydb.close()

    return HttpResponse(json, content_type="application/json")


def getData(request):
    userId = request.GET["id"]
    print(userId)
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()

    getData = "SELECT * FROM cyber_usuarios WHERE cyber_usuarios.id = ?"
    rows = cur.execute(getData,(userId)).fetchall()

    if not rows:
        json = dumps({"msg":"No registrado"})
    else:
        lista_salida = []
        for r in rows:
            d = {
                "id": r[0],
                "name": r[1],
                "password": r[2],
                "email": r[3],
                "phone": r[4],
                "school": r[5],
                "rol": r[6],
                
            }
            
            print(d)

        json = dumps(d)

    mydb.commit()
    mydb.close()

    return HttpResponse(json, content_type="application/json")


def getStats(request):
    userId = request.GET["user_id"]
    print(userId)
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()

    getData = "SELECT count() filter (where idServicio = '1') as idService, count () filter (where idServicio = '2') as idService, count (*) filter (where idServicio = '3') as idService from  cyber_reservas WHERE user_id_id = ?"
    rows = cur.execute(getData,(userId)).fetchall()

    if not rows:
        json = dumps({"msg":"No registrado"})
    else:
        lista_salida = []
        for r in rows:
            d = {
                "espacios": r[0],
                "equipos": r[1], 
                "licencias": r[2],     
            }
            
            print(d)

        json = dumps(d)

    mydb.commit()
    mydb.close()

    return HttpResponse(json, content_type="application/json")

   