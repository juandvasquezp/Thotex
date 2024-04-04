from django.db import models

# Create your models here.

class Persona(models.Model):
    Per_id = models.AutoField(primary_key=True)
    Mun_id = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    Dep_id = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    Per_tipoId = models.CharField(max_length=30)
    Per_identificacion = models.IntegerField()
    Per_nombre = models.CharField(max_length=40)
    Per_apellido = models.CharField(max_length=40)
    Per_password = models.CharField(max_length=50)
    Per_correo = models.EmailField()
    Per_telefono = models.IntegerField()

class Departamento(models.Model):
    Dep_id = models.AutoField(primary_key=True)
    Dep_nombre = models.CharField(max_length=30)

class Municipio(models.Model):
    Mun_id = models.AutoField(primary_key=True)
    Dep_id = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    Mun_nombre = models.CharField(max_length=30)
    

class Empleado():
    idEmpleado = models.IntegerField()
    departamentoId = models.IntegerField()
    municipioId = models.IntegerField()
    personaId = models.ForeignKey(Persona, on_delete=models.CASCADE)
    job = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

class Cliente(models.Model):
    id_Cliente = models.IntegerField()
    departamento_Id = models.IntegerField()
    municipio_Id = models.IntegerField()
    persona_Id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    obligacion = models.IntegerField()

class Proveedor():
    idProveedor = models.IntegerField()
    nit = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)