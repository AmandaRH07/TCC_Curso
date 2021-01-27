from django.db import models

class Vacinas(models.Model):
    id_vacinas = models.AutoField(primary_key=True) 
    tipo_vacina = models.TextField("Tipo de Vacina")
    data_vacinacao = models.DateField("Data Vacinação")
    dose = models.TextField("Dose da Vacina", blank=True)
    lote = models.TextField("Lote da Vacina", blank=True)
    local = models.TextField("Local da Vacinação", blank=True)
