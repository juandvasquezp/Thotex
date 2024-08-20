# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from .Serializer import UserSerializer, MunicipioSerializer, DepartamentoSerializer
from .models import Municipio, Departamento
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token, account_activation_token_verifier
from django.core.mail import EmailMessage

User = get_user_model()
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_active'] = False
            serializer.save()
            # Enviar correo de activacion 
            current_site = get_current_site(request)  
            mail_subject = 'Se ha enviado un enlace de activacion a tu correo'  
            message = render_to_string('acc_activate_email.html', {  
                'user': serializer,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(serializer.data['id'])),  
                'token':account_activation_token.make_token(serializer),  
            })  
            to_email = serializer.data['correo']
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return JsonResponse({'mensaje': 'Por favor confirma tu correo para completar el registro'}, safe=False)  
        else:
            return JsonResponse({'mensaje': 'Registro fallido'})


class LoginView(APIView):
    
    def post(self, request):
        
        correo = request.data['correo']
        contrasena = request.data['contrasena']

        user = authenticate(username=correo, password=contrasena)
        if user is not None:
            if user.is_active == False:
                return JsonResponse({'mensaje': 'Por favor activa tu cuenta'}, safe=False)
            login(request, user)
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            token_str = token.decode('utf-8')
            response = JsonResponse({'jwt': token_str})
            return response
        else:
            return JsonResponse({'mensaje': 'Inicio de sesion fallido'})


class UserView(APIView):

    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            return JsonResponse({'mensaje': 'No hay token'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'mensaje': 'Token expirado'})

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
        
class LogoutView(APIView):
    
        def post(self, request):
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'mensaje': 'Sesion cerrada'
            }
            return response

def activate(request, uidb64, token):  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(id=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token_verifier.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponseRedirect('https://thotex.online')  # Redirige a la página especificada
    else:
        return JsonResponse('El enlace de activacion es invalido', safe=False)

def DeleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return JsonResponse('Usuario eliminado', safe=False)
        
class MunicipioLista(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class MunicipioDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class DepartamentoLista(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoMunicipiosListView(generics.RetrieveAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    lookup_field = 'Dep_id'

    def get(self, request, *args, **kwargs):
        departamento = self.get_object()  # Obtén el objeto Departamento
        serializer = self.get_serializer(departamento)  # Serializa el departamento
        
        # Devuelve los datos en el formato deseado
        context = {
            'data': serializer.data,
        }
        
        return Response(context)
                        
        

