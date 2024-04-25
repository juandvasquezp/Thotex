from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fields = ['Prod_nombre','Prod_precio','Prod_cantidad','Prod_IVA']
    list_display = ['Prod_nombre']
    