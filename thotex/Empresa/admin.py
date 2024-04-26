from django.contrib import admin
from .models import Empresa, SedeEmpresa, Proveedor, SedeProveedor

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    fields = ['Em_NIT','Em_razonSocial','Em_matriculaMercantil','Em_estadoMatricula','Em_fechaRenovacion','Em_telefono','Em_direccion','Em_correo','Mun_nombre']
    list_display = ['Em_razonSocial']

@admin.register(SedeEmpresa)
class SedeEmpresaAdmin(admin.ModelAdmin):
    fields = ['Ems_nombre','Ems_direcion','Ems_telefono','Mun_nombre','Em_razonSocial']
    list_display = ['Ems_nombre']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    fields = ['Prov_NIT','Prov_razonSocial','Prov_direccion','Prov_telefono','Prov_correo','Mun_nombre']
    list_display = ['Prov_razonSocial']

@admin.register(SedeProveedor)
class SedeProveedorAdmin(admin.ModelAdmin):
    fields = ['Provs_nombre','Provs_direccion','Provs_telefono','Mun_nombre','Prov_razonSocial']
    list_display = ['Provs_nombre']