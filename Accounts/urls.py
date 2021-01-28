from django.urls import path 
from . import views

urlpatterns = [
    path('', views.login, name="index_login"),
    path('login/', views.login, name="index_login"),
    path('logout/', views.logout, name="index_logout"),
    path('cadastro/', views.cadastro, name="index_cadastro"),
    path('dashboard/', views.dashboard, name="index_dashboard"),
]