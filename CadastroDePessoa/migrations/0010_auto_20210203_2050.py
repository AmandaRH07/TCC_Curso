# Generated by Django 3.1.5 on 2021-02-03 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0009_remove_usuario_sangue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='historico_consultas',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='historico_familiar',
        ),
    ]