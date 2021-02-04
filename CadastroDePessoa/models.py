from django.db import models
from django.contrib.auth.models import User

from stdimage.models import StdImageField

from AlergiaIntolerancia.models import Alergias, Intolerancias 
from AvaliacaoDiaria.models import AvaliacaoDiaria
from Cirurgias.models import Cirurgias
from DoencasExistentes.models import DoencasExistentes 
from Historico.models import HistoricoConsultas, HistoricoFamiliar 
from Medicacao.models import Medicamentos
# from Sangue.models import TipoSanguineo
from Vacinas.models import Vacinas


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
   
    id_fk_cadastro_user = models.ForeignKey(User, verbose_name='CadastroUser', on_delete=models.CASCADE, default="")
    '''
    Aqui estamos fazendo as ligações entre o usuário e os dados que serão 
    cadastrados posteriormente 
    '''
    Alergias 
    alergias = models.ManyToManyField(Alergias)

    # Intolerancias
    intolerancias = models.ManyToManyField(Intolerancias)

    # Avaliação Diaria
    avaliacao_diaria = models.ManyToManyField(AvaliacaoDiaria)
    
    # Cirurgias
    cirurgias = models.ManyToManyField(Cirurgias)

    # Doenças Existentes
    doencas = models.ManyToManyField(DoencasExistentes)

    # Histórico de Consultas
    # historico_consultas = models.ManyToManyField(HistoricoConsultas)

    # Histórico Familiar
    historico_familiar = models.ManyToManyField(HistoricoFamiliar)

    # Medicação
    medicacao = models.ManyToManyField(Medicamentos)

    # Sangue
    # sangue = models.ManyToManyField(TipoSanguineo)
    
    # Vacinas
    vacinas = models.ManyToManyField(Vacinas)