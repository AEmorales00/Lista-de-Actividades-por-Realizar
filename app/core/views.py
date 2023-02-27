from django.shortcuts import render,redirect
from core.models import actividaporRealizar, usuario_asignado
from .forms import actividaporRealizarForm, usuario_asignadoForm
from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'index.html')

def obtener_persona(request):
    datos = actividaporRealizar.objects.all()
    return render(request, 'print_data.html',    
    context={
        'actividaporRealizar': datos,
    })

def obtener_tipo(request):
    tipo = actividaporRealizar.objects.all()
    return render(request, 'print_data.html',    
    context={
        'actividaporRealizar': tipo,
    })

def eliminar_dato(request, id):
    eliminar_persona = actividaporRealizar.objects.filter(id=id).first()
    eliminar_persona.status = False
    eliminar_persona.save()
    return redirect ('core:listado-persona')

def agregar_persona(request):
    if request.method=="POST":
        try:
            form = actividaporRealizarForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success('Se ha agregado correctamente')
                return redirect('core:listado-persona')
            else:
                messages.error(request, "formulario no valido")
                return redirect('core:listado-persona')
        except:
            messages.error(request, "algo salio mal")
            return redirect('core:listado-persona')
    else:
        messages.error(request,"Solo acepta method POST")
    ##
    formulario = actividaporRealizarForm
    return render(request, 'crearpersona.html', context={
        'form': formulario,
    })


class EditarPersona(UpdateView):
    model = actividaporRealizar
    template_name = 'editar_persona.html'
    form_class = actividaporRealizarForm
    success_url = reverse_lazy('core:listado-persona')



def home(request):
    return render(request, 'index.html')

def obtener_usuario(request):
    datos = usuario_asignado.objects.all()
    return render(request, 'print_data.html',    
    context={
        'usuario_asignado': datos,
    })

def obtener_usuario(request):
    tipo = usuario_asignado.objects.all()
    return render(request, 'print_data.html',    
    context={
        'usuario_asignado': tipo,
    })

def cambiar_estado_terminado(request, id):
    eliminar_persona = usuario_asignado.objects.filter(id=id).first()
    eliminar_persona.status = False
    eliminar_persona.save()
    return redirect ('core:listado-usuario')

def agregar_usuario(request):
    if request.method=="POST":
        try:
            form = usuario_asignadoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success('Se ha agregado correctamente')
                return redirect('core:listado-usuario')
            else:
                messages.error(request, "formulario no valido")
                return redirect('core:listado-usuario')
        except:
            messages.error(request, "algo salio mal")
            return redirect('core:listado-usuario')
    else:
        messages.error(request,"Solo acepta method POST")
    ##
    formulario = usuario_asignadoForm
    return render(request, 'crearusuario.html', context={
        'form': formulario,
    })


class EditarUsuario(UpdateView):
    model = actividaporRealizar
    template_name = 'editar_usuario.html'
    form_class = usuario_asignadoForm
    success_url = reverse_lazy('core:listado-usuario')