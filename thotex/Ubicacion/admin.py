from django.contrib import admin
from .models import Departamento,  Municipio

# Register your models here.

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    fields = ['Dep_nombre']
    list_display = ['Dep_nombre']


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    fields = ['Mun_nombre','Dep_nombre']
    list_display = ['Mun_nombre']

