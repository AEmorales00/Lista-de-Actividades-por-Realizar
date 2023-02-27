from django.db import models

# Create your models here.
class usuario_asignado(models.Model):
    nombres_completos = models.TextField(max_length=150)
    correo = models.EmailField()
    usuario = models.TextField(max_length=150)
    password = models.TextField(max_length=150)
    fecha_de_creacion = models.DateField()
    estados = models.TextField(default=True)  
    def __str__(self):
        return self.usuario
    
estad=[
    (1, 'Asignado'),
    (2, 'En Proceso'),
    (3, 'Terminado')
]
proces=[
    (1, 'Alta'),
    (2, 'Media'),
    (3, 'Baja')
]


class actividaporRealizar(models.Model):
    nombre = models.TextField(max_length=150)
    fecha_vencimiento = models.DateField()
    prioridad = models.IntegerField(
        null=False, blank=False,
        choices=proces,
        default=1
        )
    estado = models.IntegerField(
        null=False, blank=False,
        choices=estad,
        default=1
        )
    usuario_asig = models.ForeignKey(usuario_asignado, related_name="usario_asignado", on_delete=models.CASCADE)
    fecha_creacion= models.DateField()
    def __str__(self):
       return self.nombre