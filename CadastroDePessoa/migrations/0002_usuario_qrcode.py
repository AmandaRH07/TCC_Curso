# Generated by Django 3.1.5 on 2021-02-12 18:36

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='qrcode',
            field=stdimage.models.StdImageField(blank=True, upload_to=''),
        ),
    ]