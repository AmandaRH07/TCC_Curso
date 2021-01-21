from django.db import models


class HistoricoFamiliar(models.Model):
    GRAU_PARENTESCO = (
        ('primeiro_grau',"Primeiro Grau" ), # pais
        ('segundo_grau',"Segundo Grau" ), # irmãos e avós
        ('Terceiro_grau',"Terceiro Grau" ), # bisavô
        ('outros', "Outros" ),
    )
    id_historico_familiar = models.AutoField(primary_key=True) 
    doenca_hereditarias = models.TextField("Doenças Hereditarias", blank=True)
    tipo_doenca = models.TextField("Tipo da Doença", blank=True)
    grau_parentesco = models.CharField("Grau Parentesco", choices=GRAU_PARENTESCO, max_length=13)


class HistoricoConsultas(models.Model):
    id_historico_consultas = models.AutoField(primary_key=True) 
    lugar = models.TextField("Lugar")
    data = models.DateField("Data Consulta")
    infos_extras = models.TextField("Informações Extras", blank=True)

