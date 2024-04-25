from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .Serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):
    
    def post(self, request):
                
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    
    def post(self, request):
        
        correo = request.data['correo']
        contrasena = request.data['contrasena']

        user = authenticate(username=correo, password=contrasena)
        if user is not None:
            login(request, user)
            return JsonResponse({'mensaje': 'Inicio de sesion exitoso'})
        else:
            return JsonResponse({'mensaje': 'Inicio de sesion fallido'})
        
class LogoutView(APIView):
    
        def get(self, request):
            logout(request)
            return JsonResponse({'mensaje': 'Sesion cerrada'})
                        
                        
        

