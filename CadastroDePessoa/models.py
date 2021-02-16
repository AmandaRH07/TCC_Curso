from django.db import models
from django.contrib.auth.models import User
import uuid

from stdimage.models import StdImageField


class Usuario(models.Model):
    SEXO_CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
        ('sem_resposta', 'Prefiro não responder'),
    )

    id_usuario = models.AutoField(primary_key=True) 
    foto = StdImageField(upload_to='perfil_user', blank=True) 
    nome = models.CharField('Nome', max_length=100)
    nascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=21)
    telefone = models.CharField('Telefone', max_length=13, blank=False, default='00')
    email = models.EmailField('Email', max_length=254)
    qrcode = models.TextField('QRCode', blank=True)
    hash_user = models.UUIDField('Hash User', default=uuid.uuid4, unique=True, editable=False)
   
    id_fk_cadastro_user = models.ForeignKey(User, verbose_name='CadastroUser', on_delete=models.CASCADE, default="")
    