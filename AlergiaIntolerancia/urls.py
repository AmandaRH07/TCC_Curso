from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('alergia-intolerancia', TemplateView.as_view(template_name='alergia-intolerancia.html'), name='alergia-intolerancia'),
]