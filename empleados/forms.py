from django import forms
from .models import Persona, Empleado

class PersonaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['Per_tipoId', 'Per_id', 'Per_nombre', 'Per_apellido', 'Per_correo', 'Per_telefono', 'Mun_nombre']

