# Generated by Django 3.0.6 on 2020-05-27 17:58

from django.db import migrations, models

import clientes.models


class Migration(migrations.Migration):
    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(validators=[clientes.models.validar_data_nascimento],
                                   verbose_name='Data de Nascimento'),
        ),
    ]
