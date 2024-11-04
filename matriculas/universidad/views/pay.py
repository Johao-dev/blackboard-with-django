from django.shortcuts import redirect
from universidad.models import *
import json
from datetime import date, timedelta
from django.http import JsonResponse

#create your views here
def pagar_matricula(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        try:
            alumno = Alumnos.objects.get(codigo_alumno=data.get('codigo_alumno'))
            if (alumno):
                matricula = Matriculas.objects.get(alumno=alumno)
                carrera = alumno.carrera
                numero_ciclos = carrera.numero_ciclos

                fecha_actual = date.today()
                for ciclo in range(1, numero_ciclos + 1):
                    fecha_vencimiento = fecha_actual + timedelta(days=180 * ciclo)
                    Pagos.objects.create(
                        matricula=matricula,
                        numero_cuota=ciclo,
                        monto=565.00,
                        fecha_pago=fecha_vencimiento,
                        estado_pago='pendiente'
                    )
                
                return redirect("/universidad/login/")
        except Alumnos.DoesNotExist:
            return JsonResponse({'mensaje': 'No se encontro al alumno'})
        except Matriculas.DoesNotExist:
            return JsonResponse({'mensaje': 'No se encontro ninguna matricula'})
        

def pagar_cuota(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        cuota_id = data.get('cuota_id')
        matricula_id = data.get('matricula_id')
        try:
            matricula = Matriculas.objects.get(matricula_id=matricula_id)
            cuota = Pagos.objects.get(matricula=matricula, pagos_id=cuota_id)
            cuota.estado_pago = 'pagado'
            cuota.save()
            return JsonResponse({'redirect_url': '/universidad/blackboard/cronograma/'})
        
        except Pagos.DoesNotExist:
            return JsonResponse({'mensaje': 'No se encontro la cuota'})
        except Matriculas.DoesNotExist:
            return JsonResponse({'mensaje': 'No se encontro la matricula'})


def cargar_datos_cuota(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        request.session['cuota_id'] = data.get('cuota_id')
        request.session['matricula_id'] = data.get('matricula_id')
        return JsonResponse({'redirect_url': '/universidad/blackboard/cronograma/pago_cuota/'})
    