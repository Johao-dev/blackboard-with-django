from django.urls import path
from .views.auth import matricular, loguear
from .views.pay import pagar_matricula, pagar_cuota, cargar_datos_cuota
from .views.views import *
from .views.dashboard import *

#create your urls here
urlpatterns = [
    path('', index_view, name='index'),
    path('matricular/', matricular, name='matricular'),
    path('pago/', pago_view, name='pago'),
    path('pago_realizado/', pagar_matricula, name='pagar'),
    path('login/', login_view, name='login'),
    path('logging/', loguear, name='log'),
    path('blackboard/', blackboard_view, name='blackboard'),
    path('blackboard/cursos/', cursos_view, name='cursos'),
    path('blackboard/cronograma/', cronograma_view, name='cronograma'),
    path('blackboard/cronograma/pago_cuota/', cronograma_cuota_view, name='cronograma_cuota'),
    path('blackboard/cronograma/cargar_datos_cuota/', cargar_datos_cuota, name='cargar_datos'),
    path('blackboard/cronograma/pagar_cuota/', pagar_cuota, name='pagar_cuota'),
    path('blackboard/obtener_cursos/', obtener_cursos, name='obtener_cursos'),
    path('blackboard/obtener_cuotas/', obtener_cuotas, name='obtener_cuotas'),
]