from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('historico', TemplateView.as_view(template_name='historico.html'), name='historico')
]