from rest_framework import serializers
from . models import Espacios, Softwares, Reservas, Equipos


class EspacioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espacios
        fields = ('id', 'nombreEspacio', 'caracteristicas', 'disponibleEsp', 'capacidad', 'fechaEsp')
        
        
class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Softwares
        fields = ('id', 'fechaSoft', 'tipoSoft', 'caracteristicas', 'tiempoSoft', 'disponibleSoft')
        
        
class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservas
        fields = ('id', 'fecha', 'tipoRes', 'numS', 'estatus', 'tiempoRes')
        
class EquiposSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipos
        fields = ('id', 'fechaEq', 'tipoEq', 'caracteristicas', 'tiempoEq', 'disponibleEq')