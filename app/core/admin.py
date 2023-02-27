from django.contrib import admin

# Register your models here.
from .models import actividaporRealizar, usuario_asignado

admin.site.register(usuario_asignado)
admin.site.register(actividaporRealizar)