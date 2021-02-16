from django.db import models
from CadastroDePessoa.models import Usuario

class Cirurgias(models.Model):
    id_cirugias= models.AutoField(primary_key=True) 
    cirurgia = models.TextField('Cirurgia')
    hospital = models.CharField('Hospital', max_length=200, blank=True) 
    data_cirurgia = models.DateField('Data da Cirurgia')
    infos_extras = models.TextField('Informações Extras', blank=True)
    fk_usuario_cirurgias = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ("-data_cirurgia",)
