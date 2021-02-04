from django.db import models

from CadastroDePessoa.models import Usuario

class DoencasExistentes(models.Model):
    id_doencas_existentes = models.AutoField(primary_key=True) 
    doenca = models.CharField('Doença', max_length=200)
    ano_diagnostico = models.DateField('Ano do diagnóstico')
    exame = models.FileField(upload_to="exames", blank=True)

    fk_usuario_doencas_existentes = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")