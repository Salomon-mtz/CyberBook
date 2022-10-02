from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Espacios(models.Model):
    idEsp = models.CharField(primary_key=True, max_length=50, default=0)
    nombreEspacio = models.CharField(max_length=30, default=0)
    caracteristicas = models.CharField(max_length=50, default=0)
    tiempoEsp = models.IntegerField()
    disponibleEsp = models.BooleanField()
    capacidad = models.IntegerField()
    fechaEsp = models.CharField(max_length=30, default=0)

class Softwares(models.Model):
    idSoft = models.CharField(primary_key=True, max_length=50, default=0)
    fechaSoft = models.CharField(max_length=30, default=0)
    tipoSoft = models.CharField(max_length=20, default=0)
    caracteristicas = models.CharField(max_length=50, default=0)
    tiempoSoft = models.IntegerField()
    disponibleSoft = models.BooleanField()

class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=30, default=0)
    tipoRes = models.CharField(max_length=20, default=0)
    numS = models.CharField(max_length=50, default=0)
    estatus = models.BooleanField()
    tiempoRes = models.IntegerField()
