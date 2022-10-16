from rest_framework import serializers
from . models import Espacios, Softwares, Reservas, Equipos
from django.contrib.auth.models import User


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacios
        fields = ('id', 'nombreEspacio', 'caracteristicas', 'tiempoEsp', 'disponibleEsp', 'capacidad', 'fechaEsp')
        
        
class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwares
        fields = ('id', 'fechaSoft', 'tipoSoft', 'caracteristicas', 'tiempoSoft', 'disponibleSoft')
        
        
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = ('user_id', 'fecha', 'tipoRes', 'estatus', 'tiempoRes', 'codigo', 'idServicio')
        
class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = ('id', 'fechaEq', 'tipoEq', 'caracteristicas', 'tiempoEq', 'disponibleEq')
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'school', 'rol')