from django.urls import path
from . import views

urlpatterns = [
    path('editar-perfil', views.editar_perfil, name="editar-perfil"),
]