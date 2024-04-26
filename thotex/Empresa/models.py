from django.db import models
from Ubicacion.models import Municipio 

# Create your models here.
class Empresa(models.Model):
    estado_empresa = [
                        ('1','Activo'),
                        ('2','Cancelada'),
                        ('3','No renovada')]

    Em_codigo = models.AutoField(primary_key=True)
    Em_NIT = models.IntegerField(verbose_name='NIT')
    Em_razonSocial = models.CharField(max_length = 70, verbose_name='Razon Social')
    Em_matriculaMercantil = models.IntegerField(verbose_name="Matricula")
    Em_estadoMatricula = models.CharField(verbose_name="Estado", max_length=50)
    Em_fechaRenovacion = models.DateField(verbose_name= "Fecha de renovacion", auto_now=False, auto_now_add=False) 
    Em_telefono = models.IntegerField(verbose_name="Telefono")
    Em_direccion = models.CharField(verbose_name="Direccion", max_length=50)
    Em_correo = models.CharField(verbose_name="Correo", max_length=100)
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)

    class Meta:
        db_table = "Empresa"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.Em_razonSocial
    
class SedeEmpresa(models.Model):
    Ems_codigo = models.AutoField(primary_key=True)
    Ems_nombre = models.CharField(max_length = 100, verbose_name='Nombre')
    Ems_direcion = models.CharField(verbose_name="Direccion", max_length=50)
    Ems_telefono = models.IntegerField(verbose_name="Telefono")
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Em_razonSocial = models.ForeignKey(Empresa, verbose_name="Razon social empresa", on_delete=models.CASCADE)

    class Meta:
        db_table = "SedeEmpresa"
        verbose_name = "Sede empresa"
        verbose_name_plural = "Sede empresas"

    def __str__(self) -> str:
        return self.Ems_nombre
    
class Proveedor(models.Model):
    Prov_codigo = models.AutoField(primary_key=True)
    Prov_NIT = models.IntegerField(verbose_name='NIT proveedor')
    Prov_razonSocial = models.CharField(verbose_name="Razon social proveedor", max_length=100)
    Prov_direccion = models.CharField(verbose_name="Direccion", max_length=50)
    Prov_telefono = models.IntegerField(verbose_name="Telefono")
    Prov_correo = models.CharField(verbose_name="Correo", max_length=100)
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)

    class Meta:
        db_table = "Proveedor"
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self) -> str:
        return self.Prov_razonSocial
    
class SedeProveedor(models.Model):
    Provs_codigo = models.AutoField(primary_key=True)
    Provs_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Provs_direccion = models.CharField(verbose_name="Direccion", max_length=50)
    Provs_telefono = models.IntegerField(verbose_name="Telefono")
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Prov_razonSocial = models.ForeignKey(Proveedor, verbose_name="Razon social Proveedor", on_delete=models.CASCADE)

    class Meta:
        db_table = "SedeProveedor"
        verbose_name = "Sede Proveedor"
        verbose_name_plural = "Sede Proveedores"

    def __str__(self) -> str:
        return self.Provs_nombre