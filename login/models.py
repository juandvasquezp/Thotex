from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class User(AbstractUser):
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    username = None

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []
    

# Crear perfil según sea persona o empresa
    
# def crear_persona(sender, instance, created, **kwargs):
#     if created:
#         user_persona = Persona(Usuario=instance)
#         user_persona.save()

# post_save.connect(crear_persona, sender=User)

# def crear_empresa(sender, instance, created, **kwargs):
#     if created:
#         user_empresa = Empresa(Usuario=instance)
#         user_empresa.save()
        
# post_save.connect(crear_empresa, sender=User)

class Persona(models.Model):
    
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Per_id = models.AutoField(primary_key=True)
    Mun_id = models.ForeignKey('Municipio', on_delete=models.CASCADE, null=True)
    Per_tipoId = models.CharField(max_length=30)
    Per_identificacion = models.IntegerField()
    Per_nombre = models.CharField(max_length=40)
    Per_apellido = models.CharField(max_length=40)
    Per_telefono = models.IntegerField()
    

class Departamento(models.Model):
    
    Dep_id = models.AutoField(primary_key=True)
    Dep_nombre = models.CharField(max_length=30)
    

class Municipio(models.Model):
    
    Mun_id = models.AutoField(primary_key=True)
    Dep_id = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    Mun_nombre = models.CharField(max_length=30)