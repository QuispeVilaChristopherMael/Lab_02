from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    # Actividad 2: Encuesta
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),

    # Actividad 3 / Tarea 1: Operaciones
    path('operaciones/', views.operaciones, name='operaciones'),
    path('operaciones/calcular', views.calcular_operacion, name='calcular_operacion'),

    # Actividad 3 / Tarea 2: Cilindro
    path('cilindro/', views.cilindro, name='cilindro'),
    path('cilindro/calcular', views.calcular_cilindro, name='calcular_cilindro'),
]
