from django.db import models

# Create your models here.
class Nomina(models.Model):
    Nom_codigo = models.AutoField(primary_key=True, verbose_name="Codigo Nomina")
    Nom_fechaGeneracion = models.DateField()
    Nom_costoTotal = models.IntegerField()


class DesprendibleNomina(models.Model):
    Nms_codigo = models.AutoField(primary_key=True, verbose_name = "Codigo desprendible")
    #Emp_nit = models.ForeignKey("app.Model", verbose_name="Nit empresa", on_delete=models.CASCADE)

