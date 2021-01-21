from django.db import models

# Create your models here.

class AvaliacaoDiaria(models.Model):
    SINTOMAS_CHOICES = (
        ('dorDeCabeca', 'Dor de Cabeça'),
        ('dorNoCorpo', 'Dor no corpo'),
        ('cansaco', 'Cansaço'),
        ('dorNoEstomago', 'Dor no estômago'),
        ('inchaco', 'Inchaço'),
        ('nausea', 'Náusea'),
        ('enjoo', 'Enjôo'),
        ('faltaDeAr', 'Falta de ar'),
        ('ansiedade', 'Ansiedade'),
        ('outro', 'Outro'),
    )
    id_avaliacao_diaria = models.AutoField(primary_key=True) 
    sintomas = models.CharField('Sintomas', choices=SINTOMAS_CHOICES, max_length=15)
    observacoes = models.TextField('Observações') #verificar se precisa max_length
    # chave estrangeira para pessoa

