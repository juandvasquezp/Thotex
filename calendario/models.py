from django.db import models

# Create your models here.

class Evento(models.Model):
    todo_el_dia = models.BooleanField(default=False)
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.titulo