from django.urls import path
from . import views

urlpatterns = [
    path('avaliacao-diaria', views.index, name='index')
]