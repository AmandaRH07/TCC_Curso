from django.db import models

class Medicamentos(models.Model):
    nome = models.TextField("Nome Medicamento")
    funcao = models.TextField("Função", blank=True)
    data_inicio = models.DateField("Data de Início", blank=True)
    data_final = models.DateField("Data Final", blank=True)
    # horario = models.TimeField("Horario Medicamento")
    infos_extras = models.TextField("Informações Extras", blank=True)
    
