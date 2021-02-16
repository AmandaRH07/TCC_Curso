from django.db import models
from CadastroDePessoa.models import Usuario

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

    id_tipos_sanguineo = models.AutoField(primary_key=True) 
    tipo_sanguineo = models.CharField('Tipo Sanguíneo', choices=TIPO_SANGUINEO_CHOICES, max_length=10)
    doador = models.BooleanField('Doador', default=False)
    fk_usuario_tipo_sanguineo = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")