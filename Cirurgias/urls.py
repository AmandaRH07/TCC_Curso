from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('cirurgias', TemplateView.as_view(template_name='cirurgias.html'), name='cirurgias')
]