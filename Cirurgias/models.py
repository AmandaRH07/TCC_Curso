from django.db import models

class Cirurgias(models.Model):
    cirurgia = models.TextField('Cirurgia')
    motivo = models.TextField('Motivo', blank=True)
    hospital = models.CharField('Hospital', max_length=200, blank=True) 
    data_cirurgia = models.DateField('Data da Cirurgia')
    infos_extras = models.TextField('Informações Extras', blank=True)
    id_pessoa = models.ForeignKey('CadastroDePessoa.Usuario', verbose_name='Usuário', on_delete=models.CASCADE)