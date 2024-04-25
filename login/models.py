from django.db import models
# from thotex.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class User(AbstractUser):
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    username = None

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []
    
def crear_persona(sender, instance, created, **kwargs):
    if created:
        user_persona = Persona(User=instance)
        user_persona.save()

post_save.connect(crear_persona, sender=User)

class Persona(models.Model):
    
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Per_id = models.AutoField(primary_key=True)
    Mun_id = models.ForeignKey('Municipio', on_delete=models.CASCADE)
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