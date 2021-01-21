from django.db import models

class DoencasExistentes(models.Model):
    id_doencas_existentes = models.AutoField(primary_key=True) 
    doenca = models.CharField('Doença', max_length=200)
    ano_diagnostico = models.DateField('Ano do diagnóstico')
    exame = models.FileField(upload_to="midias/exames", blank=True)