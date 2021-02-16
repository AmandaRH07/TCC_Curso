from django.db import models
from CadastroDePessoa.models import Usuario

class Medicamentos(models.Model):
    id_medicamentos = models.AutoField(primary_key=True) 
    nome = models.CharField('Nome', max_length=100, default="")
    funcao = models.TextField("Função", blank=True)
    data_inicio = models.DateField("Data de Início", blank=True)
    data_final = models.DateField("Data Final", blank=True)

    fk_user_medicacao = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ("-data_inicio",)