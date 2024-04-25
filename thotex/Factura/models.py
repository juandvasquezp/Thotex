from django.db import models
from Usuarios.models import Cliente

# Create your models here.
class Factura(models.Model):
    Fac_codigo = models.AutoField(primary_key=True, verbose_name="Factura codigo")
    Fac_fechaGeneracion = models.DateField(verbose_name='Fecha generacion', auto_now_add=True)
    Fac_subtotal = models.DecimalField(verbose_name="Subtotal", decimal_places=2, max_digits=15)
    Fac_precioTotal = models.DecimalField(verbose_name="Precio total", decimal_places=2, max_digits=15)
    Fac_IVA = models.DecimalField(verbose_name="IVA", decimal_places=2, max_digits=3) #tipo de dato (IGUAL PRODUCTO)
    Cl_codigo = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")

    class Meta:
        db_table = "Factura"
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self) -> str:
        return self.Fac_codigo