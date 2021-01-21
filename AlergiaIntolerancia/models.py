from django.db import models

class Alergias(models.Model):
    id_alergias = models.AutoField(primary_key=True) 
    tipo = models.TextField("Tipo de Alergia")
    causador = models.TextField("Tipo de Causador")

class Intolerancias(models.Model):
    id_intolerancias = models.AutoField(primary_key=True) 
    tipo = models.TextField("Tipo de Alergia")
    causador = models.TextField("Tipo de Causador")