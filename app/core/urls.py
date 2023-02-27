from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('listado-persona/', obtener_persona, name='listado-persona'),
    path('eliminar/<int:id>', eliminar_dato, name='eliminar'),
    path('crear-persona/', agregar_persona, name='crear-persona'),
    path('editar/<int:pk>', EditarPersona.as_view(), name='editar_persona'),
    path('crear-usuario/', agregar_usuario, name='crear-usuario')
 
    
]