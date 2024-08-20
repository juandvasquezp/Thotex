# Generated by Django 5.0.3 on 2024-08-20 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_producto_emp_codigo'),
        ('terceros', '0004_alter_proveedor_prov_telefono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Emp_codigo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='terceros.cliente', verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]