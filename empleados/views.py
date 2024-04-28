from rest_framework import generics
from .models import Empleado
from .Serializer import *

# Create your views here.
class EmpleadoLista(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
class EmpleadoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer   
    
    
    
