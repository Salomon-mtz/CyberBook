from django.contrib import admin
from .models import Equipos, Espacios
from .models import Softwares
from .models import Reservas

class EspaciosAdmin(admin.ModelAdmin):
    readonly_fields = ('idEsp',)

class SoftwareAdmin(admin.ModelAdmin):
    readonly_fields = ('idSoft',)

class EquiposAdmin(admin.ModelAdmin):
    readonly_fields = ('idEq',)

admin.site.register(Espacios, EspaciosAdmin)
admin.site.register(Softwares)
admin.site.register(Reservas)
admin.site.register(Equipos)
# Register your models here.
