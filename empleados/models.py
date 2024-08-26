from django.db import models
from login.models import Municipio, Departamento, User
from django.core.validators import MaxValueValidator, MinValueValidator
# create your models here.

class Persona(models.Model):

    tipoId = [
        ('Cédula de ciudadanía', 'Cédula de ciudadanía'),
        ('Tarjeta de identidad', 'Tarjeta de identidad'),
        ('Cédula de extranjería', 'Cédula de extranjería'),
        ('Pasaporte', 'Pasaporte'),
        ('Registro Civil', 'Registro Civil'),
        ('Tarjeta de Extranjería', 'Tarjeta de Extranjería'),
        ('Documento de identificación extranjero', 'Documento de identificación extranjero'),
        ('PEP', 'PEP'),
        ('NUIP', 'NUIP'),
        ('NIT', 'NIT'),
    ]


    Per_codigo = models.AutoField(primary_key = True)
    Per_tipoId = models.CharField(max_length = 38, choices = tipoId, verbose_name='Tipo de identificacion')
    Per_id = models.CharField(max_length = 50, verbose_name='Identificacion')
    Per_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Per_apellido = models.CharField(max_length = 50, verbose_name='Apellido')
    Per_correo = models.EmailField(max_length = 50, verbose_name='Correo', unique=True)
    Per_telefono = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='Telefono')
    # Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)

    class Meta:
        db_table = "Persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self) -> str:
        return self.Per_nombre
    
class Empleado(models.Model):

    tipoContrato = [
        ('Término Fijo', 'Término Fijo'),
        ('Término Indefinido', 'Término Indefinido'),
        ('Obra o Labor', 'Obra o Labor'),
        ('Aprendizaje', 'Aprendizaje'),
        ('Prácticas o Pasantías', 'Prácticas o Pasantías'),
    ]

    tipoTrabajador = [
        ('Dependiente', 'Dependiente'),
        ('Servicio doméstico', 'Servicio doméstico'),
        ('Madre comunitaria', 'Madre comunitaria'),
        ('Aprendices del Sena en etapa lectiva', 'Aprendices del Sena en etapa lectiva'),
        ('Funcionarios públicos sin tope máximo de IBC', 'Funcionarios públicos sin tope máximo de IBC'),
        ('Aprendices del SENA en etapa productiva', 'Aprendices del SENA en etapa productiva'),
        ('Estudiantes de postgrado en salud', 'Estudiantes de postgrado en salud'),
        ('Profesor de establecimiento particular', 'Profesor de establecimiento particular'),
        ('Estudiantes aportes solo riesgos laborales', 'Estudiantes aportes solo riesgos laborales'),
        ('Dependiente entidades o universidades públicas con régimen especial en salud', 'Dependiente entidades o universidades públicas con régimen especial en salud'),
        ('Cooperados o pre cooperativas de trabajo asociado', 'Cooperados o pre cooperativas de trabajo asociado'),
        ('Trabajador dependiente de entidad beneficiaria del sistema general de participaciones - aportes patronales', 'Trabajador dependiente de entidad beneficiaria del sistema general de participaciones - aportes patronales'),
        ('Trabajador de tiempo parcial', 'Trabajador de tiempo parcial'),
        ('Pre pensionado con aporte voluntario a salud', 'Pre pensionado con aporte voluntario a salud'),
        ('Pre pensionado de entidad en liquidación', 'Pre pensionado de entidad en liquidación'),
        ('Estudiantes de prácticas laborales en el sector público', 'Estudiantes de prácticas laborales en el sector público'),
    ]

    Emp_codigo = models.AutoField(primary_key=True)
    Emp_tipoContrato = models.CharField(max_length = 30, choices = tipoContrato, verbose_name='Tipo de contrato')
    Emp_tipoTrabajador = models.CharField(max_length = 106, choices = tipoTrabajador, verbose_name='Tipo de trabajador')
    Emp_cargo = models.CharField(max_length = 60, verbose_name='cargo')
    Emp_salario = models.IntegerField(verbose_name="salario")
    Emp_fechaingreso = models.DateField(verbose_name="fecha de ingreso", auto_now_add=True)
    Persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class meta:
        db_table = "Empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self) -> str:
        return self.Persona.Per_nombre
