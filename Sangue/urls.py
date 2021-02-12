from django.urls import path
from . import views

urlpatterns = [
    path("sangue", views.sangue, name="sangue"),
    path("tipo-sanguineo", views.sangue_detail, name="sangue_detail"),
]