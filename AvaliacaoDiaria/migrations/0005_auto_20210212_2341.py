# Generated by Django 3.1.5 on 2021-02-13 02:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AvaliacaoDiaria', '0004_auto_20210212_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaodiaria',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 13, 2, 41, 45, 90536, tzinfo=utc), verbose_name='Data '),
        ),
    ]
