from django.db import models
from empleados.models import Persona

# Create your models here.


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
