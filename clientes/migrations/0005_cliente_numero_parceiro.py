# Generated by Django 3.0.6 on 2020-05-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20200527_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='numero_parceiro',
            field=models.CharField(blank=True, max_length=15, verbose_name='Número de Parceiro'),
        ),
    ]
