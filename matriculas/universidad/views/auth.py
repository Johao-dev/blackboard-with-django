from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from universidad.models import *
from datetime import date
from django.db import transaction
from universidad.utils import *
import json

"""
Endpoints para matricula.html
"""
def matricular(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        # objetos a persistir
        alumno = Alumnos()
        try:
            nombre_carrera = data.get('career')
            carrera = Carreras.objects.get(nombre=nombre_carrera)
        except Carreras.DoesNotExist:
            return HttpResponse('Carrera no encontrada')
        
        matricula = Matriculas()

        #datos del template
        alumno.nombre_completo = data.get('fullName')
        alumno.dni = data.get('dni')
        alumno.telefono = data.get('phone')
        alumno.correo = data.get('email')
        alumno.carrera = carrera

        matricula.fecha_matricula = date.today()
        matricula.alumno = alumno
        matricula.carrera = carrera

        # estos datos son not null en la bd, por ahora
        # son ficticios, luego se actualizaran
        alumno.contrasenia = generate_student_password()
        alumno.codigo_alumno = generate_student_code()
        alumno.direccion = 'direccion_default'
        alumno.sexo = 'sexo_default'
        alumno.fecha_nacimiento = date.today()
        
        # generando datos de pago
        codigo = generate_paycode()
        importe = generate_amount()
        fecha_vencimiento = generate_expiration_date()
        correo_estudiantil = generate_email_student()
        # agrego el correo estudiantil
        alumno.correo_estudiantil = correo_estudiantil
        
        # persistir en la base de datos usando transaccion
        with transaction.atomic():
            alumno.save()
            matricula.save()
        
        # redireccionar a la vista de pago
        return redirect(
    f"/universidad/pago/?matricula_id={matricula.matricula_id}&alumno_id={alumno.alumno_id}&codigo_pago={codigo}&importe={importe}&fecha_vencimiento={fecha_vencimiento}&correo_estudiantil={correo_estudiantil}&contrasena_estudiantil={alumno.contrasenia}&codigo_alumno={alumno.codigo_alumno}")


def loguear(request):
    if request.method == "POST":
        data = json.loads(request.body)
        correo = data.get('correo')
        contrasena = data.get('contrasena')
        try:
            alumno = Alumnos.objects.get(correo_estudiantil=correo, contrasenia=contrasena)
            carrera = alumno.carrera
            cursos = Cursos.objects.filter(carrera=carrera)

            request.session['alumno'] = {
                'nombre_completo': alumno.nombre_completo,
                'genero': alumno.sexo,
                'correo_institucional': alumno.correo_estudiantil,
                'codigo_alumno': alumno.codigo_alumno,
                'fecha_nacimiento': str(alumno.fecha_nacimiento)
            }
            request.session['nombre_carrera'] = carrera.nombre
            request.session['cursos'] = [curso.nombre for curso in cursos]
            
            return JsonResponse({'redirect_url': '/universidad/blackboard/'})

        except Alumnos.DoesNotExist:
            return JsonResponse({'mensaje': 'Alumno no encontrado'})