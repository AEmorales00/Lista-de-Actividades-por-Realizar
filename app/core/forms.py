from django import forms
from .models import usuario_asignado, actividaporRealizar

class usuario_asignadoForm(forms.ModelForm):
    class Meta:
        model =usuario_asignado
        fields = '__all__'

class actividaporRealizarForm(forms.ModelForm):
    class Meta:
        model =actividaporRealizar
        fields = '__all__'