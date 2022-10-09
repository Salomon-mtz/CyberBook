from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Espacios(models.Model):
    id = models.AutoField(primary_key=True)
    nombreEspacio = models.CharField(max_length=30, default=0)
    caracteristicas = models.CharField(max_length=500, default=0)
    tiempoEsp = models.CharField(max_length=500, default=0)
    disponibleEsp = models.CharField(max_length=500, default=0)
    capacidad = models.CharField(max_length=500, default=0)
    fechaEsp = models.CharField(max_length=30, default=0)
    imageEsp = models.ImageField(upload_to='cyber/static', default='')

class Softwares(models.Model):
    id = models.AutoField(primary_key=True)
    fechaSoft = models.CharField(max_length=30, default=0)
    tipoSoft = models.CharField(max_length=20, default=0)
    caracteristicas = models.CharField(max_length=50, default=0)
    tiempoSoft = models.CharField(max_length=500, default=0)
    disponibleSoft = models.CharField(max_length=500, default=0)
    imageSoft = models.ImageField(upload_to='cyber/static', default='')

class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=30, default=0)
    tipoRes = models.CharField(max_length=20, default=0)
    numS = models.CharField(max_length=50, default=0)
    estatus = models.CharField(max_length=500, default=0)
    tiempoRes = models.CharField(max_length=500, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    fechaEq = models.CharField(max_length=30, default=0)
    tipoEq = models.CharField(max_length=20, default=0)
    caracteristicas = models.CharField(max_length=50, default=0)
    tiempoEq = models.CharField(max_length=500, default=0)
    disponibleEq = models.CharField(max_length=500, default=0)
    imageEq = models.ImageField(upload_to='cyber/static', default='')