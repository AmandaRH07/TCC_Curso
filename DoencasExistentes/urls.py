from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('doencas-existentes', TemplateView.as_view(template_name='doencas-existentes.html'), name='doencas-existentes')
]