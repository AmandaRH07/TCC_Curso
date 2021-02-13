from django.urls import path
from . import views

urlpatterns = [
    path('perfil', views.perfil, name="perfil"),
    path('informacoes', views.informacoes, name="informacoes"),
    path('pdf_view/<uuid:hash_user>/', views.pdf_view, name="pdf_view"),
    path('pdf_download', views.pdf_download, name="pdf_download"),
    path('qrcode', views.qrcode, name="qrcode"),
    
]