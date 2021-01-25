from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('login', TemplateView.as_view(template_name='login.html'), name='login')
]