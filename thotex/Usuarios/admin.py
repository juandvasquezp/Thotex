from django.contrib import admin
from .models import Persona, Empleado, Cliente

# Register your models here.
@admin.register
class PersonaAdmin(Persona):
    fields = ['Per_TipoId','Per_id','Per_nombre','Per_apellido','Per_correo','Per_telefono','Mun_nombre']
    list_display = ['Per_nombre']

@admin.register
class EmpleadoAdmin(Empleado):
    fields = ['Emp_cargo','Emp_salario','Emp_fechaIngreso','Per_nombre']
    list_display = ['Per_nombre']

@admin.register
class ClienteAdmin(Cliente):
    fields = ['Cl_obligacion','Per_nombre']
    list_display = ['Per_nombre']
