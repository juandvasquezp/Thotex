from django.db import models
from Empresa.models import Empresa
from Usuarios.models import Empleado

# Create your models here.
class Nomina(models.Model):
    Nom_codigo = models.AutoField(primary_key=True, verbose_name="Codigo Nomina")
    Nom_fechaGeneracion = models.DateField(auto_now_add=True, verbose_name="Fecha")
    Nom_costoTotal = models.IntegerField(verbose_name="Costo total")

    class Meta:
        db_table = "Nomina"
        verbose_name = "Nomina"
        verbose_name_plural = "Nominas"

    def __str__(self) -> str:
        return self.Nom_fechaGeneracion

class DesprendibleNomina(models.Model):
    Nms_codigo = models.AutoField(primary_key=True, verbose_name = "Codigo desprendible")
    Nom_fechaGeneracion = models.ForeignKey(Nomina, verbose_name="Fecha de generacion", on_delete=models.CASCADE)
    Emp_codigo = models.ForeignKey(Empleado, verbose_name= "Empleado", on_delete=models.CASCADE)

    class Meta:
        db_table = "Desprendible de Nomina"
        verbose_name = "Desprendible de Nomina"
        verbose_name_plural = "Desprendibles de Nomina"

    def __str__(self) -> str:
        return self.Nom_fechaGeneracion
    