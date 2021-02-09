from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('historico', views.historico_consultas, name='historico'),
    path('historico/<int:pk>', views.historico_consultas_detail, name='historico_consultas_detail'),
    path('historico-consulta-delete/<int:pk>', views.historico_consultas_delete, name='historico_consultas_delete'),


    path('historico_familiar', views.historico_familiar, name='historico-familiar'),
]