from django.shortcuts import render
from universidad.utils import *
# Create your views here.

def index_view(request):
    return render(request, 'universidad/matricula.html')


def pago_view(request):
    contexto = {
        'matricula_id': request.GET.get('matricula_id'),
        'alumno_id': request.GET.get('alumno_id'),
        'codigo_pago': request.GET.get('codigo_pago'),
        'importe': request.GET.get('importe'),
        'fecha_vencimiento': request.GET.get('fecha_vencimiento'),
        'correo_estudiantil': request.GET.get('correo_estudiantil'),
        'contrasena_estudiantil': request.GET.get('contrasena_estudiantil'),
        'codigo_alumno': request.GET.get('codigo_alumno'),
    }
    return render(request, 'universidad/pago.html', contexto)


def login_view(request):
    return render(request, 'universidad/login.html')


def blackboard_view(request):
    contexto = {
        'alumno': request.session.get('alumno', {}),
        'carrera': request.session.get('nombre_carrera'),
        'cursos': request.session.get('cursos', [])
    }
    return render(request, 'universidad/blackboard.html', contexto)


def cursos_view(request):
    contexto = {
        'cursos': request.session.get('cursos', []),
    }
    return render(request, 'universidad/cursos.html', contexto)


def cronograma_view(request):
    contexto = {
        'cuotas': request.session.get('cuotas', []),
    }
    return render(request, 'universidad/cronograma.html', contexto)

def cronograma_cuota_view(request):
    contexto = {
        'codigo_pago': generate_paycode(),
        'importe': str(generate_amount()),
        'fecha_vencimiento': str(generate_expiration_date()),
        'cuota_id': request.session.get('cuota_id'),
        'matricula_id': request.session.get('matricula_id')
    }
    return render(request, 'universidad/pagocuota.html', contexto)