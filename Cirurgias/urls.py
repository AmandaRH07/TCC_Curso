from django.urls import path
from django.views.generic import TemplateView
from .views import cirurgia

urlpatterns = [
    path('cirurgias', cirurgia, name='cirurgias')
]