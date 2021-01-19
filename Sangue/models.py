from django.db import models

class TipoSanguineo(models.Model):
    TIPO_SANGUINEO_CHOICES = (
        ('aPositivo', 'A+'),
        ('aNegativo', 'A-'),
        ('bPositivo', 'B+'),
        ('bNegativo', 'B-'),
        ('abPositivo', 'AB+'),
        ('abNegativo', 'AB-'),
        ('oPositivo', 'O+'),
        ('oNegativo', 'O-'),
    )

    tipo_sanguineo = models.CharField('Tipo Sanguíneo', choices=TIPO_SANGUINEO_CHOICES, max_length=10)
    doador = models.BooleanField('Doador', default=False)
    historico_doacoes = models.TextField('Histórico de Doações')