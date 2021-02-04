from django.db import models
from CadastroDePessoa.models import Usuario

class Vacinas(models.Model):
    id_vacinas = models.AutoField(primary_key=True) 
    tipo_vacina = models.TextField("Tipo de Vacina")
    data_vacinacao = models.DateField("Data Vacinação")
    dose = models.TextField("Dose da Vacina", blank=True)
    lote = models.TextField("Lote da Vacina", blank=True)
    local = models.TextField("Local da Vacinação", blank=True)
    fk_usuario_vacinas = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
