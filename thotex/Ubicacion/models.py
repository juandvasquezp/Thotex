from django.db import models

# Create your models here.
class Departamento(models.Model):
    Dep_codigo = models.AutoField(primary_key=True)
    Dep_nombre = models.CharField(max_length = 50, verbose_name='Nombre')

    class Meta:
        db_table = "Departamento"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self) -> str:
        return self.Dep_nombre

class Municipio(models.Model):
    Mun_codigo = models.AutoField(primary_key=True)
    Mun_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Dep_nombre = models.ForeignKey(Departamento, on_delete=models.CASCADE) #AQUI SE PRODUCE EL ERROr / aparicion en admin

    class Meta:
        db_table = "Municipio"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self) -> str:
        return self.Mun_nombre