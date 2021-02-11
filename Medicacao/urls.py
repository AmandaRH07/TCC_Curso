from django.urls import path
from .views import medicacao, medicacao_detail, medicacao_delete


urlpatterns = [
    path('medicacao', medicacao, name='medicacao'),
    path('medicacao/<int:pk>', medicacao_detail, name="medicacao_detail"),
    path('medicacao-delete/<int:pk>', medicacao_delete, name="medicacao_delete"),

]