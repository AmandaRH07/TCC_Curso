from django.urls import path
from django.views.generic import TemplateView
from .views import cirurgia, cirurgia_detail, cirurgia_delete

urlpatterns = [
    path('cirurgias', cirurgia, name='cirurgias'),
    path('cirurgia/<int:pk>', cirurgia_detail, name="cirurgia_detail"),
    path('cirurgia-delete/<int:pk>', cirurgia_delete, name="cirurgia_delete"),
]