from django.db import models

class Cirurgias(models.Model):
    id_cirugias= models.AutoField(primary_key=True) 
    cirurgia = models.TextField('Cirurgia')
    hospital = models.CharField('Hospital', max_length=200, blank=True) 
    data_cirurgia = models.DateField('Data da Cirurgia')
    infos_extras = models.TextField('Informações Extras', blank=True)
