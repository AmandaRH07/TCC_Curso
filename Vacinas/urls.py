from django.urls import path
from . import views
from .views import vacinas

urlpatterns = [
    path('vacinas', vacinas, name="vacinas")
]