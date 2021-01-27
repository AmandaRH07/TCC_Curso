from django.urls import path
from . import views

urlpatterns = [
    path('vacinas', views.vacinas, name="vacinas")
]