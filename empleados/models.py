from django.db import models
from login.models import Municipio, Departamento, User
from django.core.validators import MaxValueValidator, MinValueValidator
# create your models here.

class Persona(models.Model):

    tipoId = [
        (1, 'Cédula de ciudadanía'),
        (2, 'Tarjeta de identidad'),
        (3, 'Cédula de extranjería'),
        (4, 'Pasaporte'),
        (5, 'Registro Civil'),
        (6, 'Tarjeta de Extranjería'),
        (7, 'Documento de identificación extranjero'),
        (8, 'PEP'),
        (9, 'NUIP'),
        (10, 'NIT'),
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
        (1, 'Término Fijo'),
        (2, 'Término Indefinido'),
        (3, 'Obra o Labor'),
        (4, 'Aprendizaje'),
        (5, 'Prácticas o Pasantías'),
    ]

    tipoTrabajador = [
        (1, 'Dependiente'),
        (2, 'Servicio doméstico'),
        (3, 'Madre comunitaria'),
        (4, 'Aprendices del Sena en etapa lectiva'),
        (5, 'Funcionarios públicos sin tope máximo de IBC'),
        (6, 'Aprendices del SENA en etapa productiva'),
        (7, 'Estudiantes de postgrado en salud'),
        (8, 'Profesor de establecimiento particular'),
        (9, 'Estudiantes aportes solo riesgos laborales'),
        (10, 'Dependiente entidades o universidades públicas con régimen especial en salud'),
        (11, 'Cooperados o pre cooperativas de trabajo asociado'),
        (12, 'Trabajador dependiente de entidad beneficiaria del sistema general de participaciones - aportes patronales'),
        (13, 'Trabajador de tiempo parcial'),
        (14, 'Pre pensionado con aporte voluntario a salud'),
        (15, 'Pre pensionado de entidad en liquidación'),
        (16, 'Estudiantes de prácticas laborales en el sector público'),
    ]

    frecuenciaPago = [
        (1, 'Quincenal'),
        (2, 'Mensual'),
    ]

    subtipoTrabajador = [
        (1, 'Dependiente pensionado por vejez activo'),
    ]

    nivelDeRiesgo = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
    ]

    area = [
        (1, 'Administrativa'),
        (2, 'Operativa'),
        (3, 'Comercial'),
    ]

    Emp_codigo = models.AutoField(primary_key=True)
    Emp_tipoContrato = models.CharField(max_length = 30, choices = tipoContrato, verbose_name='Tipo de contrato')
    Emp_tipoTrabajador = models.CharField(max_length = 106, choices = tipoTrabajador, verbose_name='Tipo de trabajador')
    Emp_subtipoTrabajador = models.CharField(max_length = 106, choices=subtipoTrabajador, verbose_name='Subtipo de trabajador')
    Emp_cargo = models.CharField(max_length = 60, verbose_name='cargo')
    Emp_area = models.CharField(max_length = 30, choices=area, verbose_name='Area')
    Emp_diasVacacionesAcumulados = models.IntegerField(verbose_name="dias de vacaciones acumulados")
    Emp_salario = models.IntegerField(verbose_name="salario")
    Emp_auxilioTransporte = models.BooleanField(verbose_name="auxilio de transporte")
    Emp_salarioIntegral = models.BooleanField(verbose_name="salario integral")
    Emp_frecuenciaPago = models.CharField(max_length = 30, choices=frecuenciaPago, verbose_name='Frecuencia de pago')
    Emp_nivelDeRiesgo = models.CharField(max_length = 30, choices=nivelDeRiesgo, verbose_name='Nivel de riesgo')
    Emp_sabadoLaboral = models.BooleanField(verbose_name="sabado laboral")
    Emp_fechaingreso = models.DateField(verbose_name="fecha de ingreso", auto_now_add=True)
    Emp_fechaFinContrato = models.DateField(verbose_name="fecha fin de contrato")
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Emp_direccion = models.CharField(max_length = 60, verbose_name='Direccion')
    Persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class meta:
        db_table = "Empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self) -> str:
        return self.Persona.Per_nombre
