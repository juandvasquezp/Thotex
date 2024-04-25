from django.contrib import admin
from .models import Factura

# Register your models here.
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    fields = ['Fac_Subtotal','Fac_precioTotal','Fac_IVA']
    list_display = ['Fac_precioTotal']
