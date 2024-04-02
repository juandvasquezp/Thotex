from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.views import View
import json


@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(View):
    def post(self, request):
        # Parse the JSON body of the request
        data = json.loads(request.body)
        name = data.get('name')
        last_name = data.get('lastName')
        email = data.get('email')
        phone_number = data.get('phoneNumber')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')
        checked_terms = data.get('checkedTerms')

        # Validar los datos
        if not all([name, last_name, email, phone_number, password, confirm_password, checked_terms]):
            return JsonResponse({'status': 'error', 'message': 'Todos los campos son requeridos'})

        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': ''})

        if User.objects.filter(username=email).exists():
            return JsonResponse({'status': 'error', 'message': ''})

        # Crear el usuario
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name, last_name=last_name)
        user.save()

        #Confirmar la operación exitosa
        return JsonResponse({'status': 'success', 'message': 'Usuario registrado con éxito'})

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        # Parse the JSON body of the request
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Usuario loggeado con éxito'})
        else:
            # Return an error message
            return JsonResponse({'status': 'error', 'message': 'Credenciales inválidas'})
