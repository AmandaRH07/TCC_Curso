from django.urls import path
from . import views

urlpatterns = [
    path('medicacao', views.medicacao, name='medicacao')
]