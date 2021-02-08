from django.urls import path
from django.views.generic import TemplateView

from .views import doencas_existentes, doencas_existentes_detail, doencas_existentes_delete

urlpatterns = [
    path('doencas-existentes', doencas_existentes, name='doencas-existentes'),
    path('doencas-existentes/<int:pk>', doencas_existentes_detail, name='doencas_existentes_detail'),
    path('doencas-existentes-delete/<int:pk>', doencas_existentes_delete, name='doencas_existentes_delete'),

]