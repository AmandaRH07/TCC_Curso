# Generated by Django 3.1.5 on 2021-02-08 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Historico', '0004_historicofamiliar_doenca_cronica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicofamiliar',
            name='doenca_cronica',
        ),
    ]
