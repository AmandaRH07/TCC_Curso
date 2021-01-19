from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
        ('sem_resposta', 'Prefiro não responder'),
    )

    foto = models.ImageField(upload_to='', blank=True)
    nome = models.CharField('Nome', max_length=100)
    nascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=21)

    email = models.EmailField('Email', max_length=254)
    senha = models.CharField('Senha', min_length=8, max_length=40)