from django.urls import path
from django.views.generic import TemplateView

from .views import doencas_existentes

urlpatterns = [
    path('doencas-existentes', doencas_existentes, name='doencas-existentes')
]