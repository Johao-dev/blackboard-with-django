from django.http import JsonResponse
from universidad.models import *
import json

# create your views here
def obtener_cursos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            alumno = Alumnos.objects.get(codigo_alumno=data['codigo_alumno'])
            cursos = Cursos.objects.filter(carrera=alumno.carrera)

            request.session['cursos'] = [
                {
                    'nombre_curso': curso.nombre,
                    'codigo_curso': curso.cursos_id,
                }
                for curso in cursos
            ]
            return JsonResponse({'redirect_url': '/universidad/blackboard/cursos/'})
        
        except Alumnos.DoesNotExist:
            return JsonResponse({'mensaje':'Alumno no encontrado'}, status=404)
        except Cursos.DoesNotExist:
            return JsonResponse({'mensaje':'Curso no disponible'}, status=404)
        except Matriculas.DoesNotExist:
            return JsonResponse({'mensaje':'Matricula no registrada'}, status=404)

def obtener_cuotas(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            alumno = Alumnos.objects.get(codigo_alumno=data['codigo_alumno'])
            matricula = Matriculas.objects.get(alumno=alumno)
            pagos = Pagos.objects.filter(matricula=matricula)

            request.session['cuotas'] = [
                {
                    'cuota': pago.numero_cuota,
                    'importe': pago.monto,
                    'fecha_vencimiento': str(pago.fecha_pago),
                    'estado_cuota': pago.estado_pago,
                    'cuota_id': pago.pagos_id,
                    'matricula_id': pago.matricula.matricula_id
                }
                for pago in pagos
            ]
            return JsonResponse({'redirect_url': '/universidad/blackboard/cronograma/'})
        
        except Alumnos.DoesNotExist:
            return JsonResponse({'mensaje':'Alumno no encontrado'}, status=404)
        except Matriculas.DoesNotExist:
            return JsonResponse({'mensaje':'Matricula no registrada'}, status=404)
        except Pagos.DoesNotExist:
            return JsonResponse({'mensaje':'Cuotas no disponibles'}, status=404)
        