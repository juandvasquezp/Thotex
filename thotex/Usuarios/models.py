from django.db import models
from Ubicacion.models import Departamento, Municipio

# Create your models here.
class Persona(models.Model):

    tipoId = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    ]

    Per_codigo = models.AutoField(primary_key = True)
    Per_tipoId = models.CharField(max_length = 30, choices = tipoId, verbose_name='Tipo de identificacion')
    Per_id = models.CharField(max_length = 50, verbose_name='Identificacion')
    Per_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Per_apellido = models.CharField(max_length = 50, verbose_name='Apellido')
    Per_correo = models.EmailField(max_length = 50, verbose_name='Correo', unique=True)
    Per_telefono = models.IntegerField(verbose_name='Telefono')
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Dep_nombre = models.ForeignKey(Departamento, verbose_name="Departamento", on_delete=models.CASCADE)

    class Meta:
        db_table = "Persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self) -> str:
        return self.Per_nombre

class Empleado(models.Model):
    Emp_codigo = models.AutoField(primary_key=True)
    Emp_cargo = models.CharField(max_length = 60, verbose_name='Cargo')
    Emp_salario = models.IntegerField(verbose_name="Salario")
    Emp_fechaIngreso = models.DateField(verbose_name="Fecha de ingreso", auto_now_add=True)
    Per_nombre = models.ForeignKey(Persona, on_delete=models.CASCADE) 

    class Meta:
        db_table = "Empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self) -> str:
        return self.Per_nombre
    
class Cliente(models.Model):
    Cl_codigo = models.AutoField(primary_key=True)
    Cl_obligacion = models.CharField(verbose_name="Obligacion tributaria", max_length=100)
    Per_nombre = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        db_table = "Cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.Per_nombre