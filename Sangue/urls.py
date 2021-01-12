from django.urls import path
from . import views

urlpatterns = [
    path("sangue", views.sangue, name="sangue"),
]