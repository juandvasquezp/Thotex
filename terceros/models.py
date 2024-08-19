from django.db import models
from empleados.models import Persona, Municipio, User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Cliente(models.Model):
    Cl_codigo = models.AutoField(primary_key=True)
    Cl_nombre = models.CharField(max_length=50, verbose_name='Nombre')
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class Meta:
        db_table = "Cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.Cl_nombre


class Proveedor(models.Model):
    Prov_codigo = models.AutoField(primary_key=True)
    Prov_NIT = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='NIT proveedor')
    Prov_razonSocial = models.CharField(verbose_name="Razon social proveedor", max_length=100)
    Prov_direccion = models.CharField(verbose_name="Direccion", max_length=50)
    Prov_telefono = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='Telefono')
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
    Provs_telefono = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='Telefono')
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Prov_razonSocial = models.ForeignKey(Proveedor, verbose_name="Razon social Proveedor", on_delete=models.CASCADE)

    class Meta:
        db_table = "SedeProveedor"
        verbose_name = "Sede Proveedor"
        verbose_name_plural = "Sede Proveedores"

    def __str__(self) -> str:
        return self.Provs_nombre
