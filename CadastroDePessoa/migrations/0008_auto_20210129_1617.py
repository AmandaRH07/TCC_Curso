# Generated by Django 3.1.5 on 2021-01-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0007_auto_20210129_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default='00', max_length=13, verbose_name='Telefone'),
        ),
    ]
