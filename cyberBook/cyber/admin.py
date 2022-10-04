from django.contrib import admin
from .models import Espacios
from .models import Softwares
from .models import Reservas

admin.site.register(Espacios)
admin.site.register(Softwares)
admin.site.register(Reservas)
# Register your models here.
