from django.db import models

class DoencasExistentes(models.Model):
    doenca = models.CharField('Doença', max_length=200)
    ano_diagnostico = models.DateField('Ano do diagnóstico')
    exame = models.FileField(upload_to="", blank=True)
