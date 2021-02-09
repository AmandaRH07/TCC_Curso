from django.urls import path
from . import views
from .views import vacinas, vacinas_detail, delete_vacina

urlpatterns = [
    path('vacinas', vacinas, name="vacinas"),
    path('vacina_detail/<int:pk>', vacinas_detail, name="vacina_detail"),
    path('delete_vacina/<int:pk>', delete_vacina, name="delete_vacina"),
]