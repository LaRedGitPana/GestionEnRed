# Generated by Django 4.2.5 on 2023-10-09 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_relacionthc_contracttype_relacionthc_modalidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='relacionthc',
            name='cargo',
            field=models.CharField(default='Empleado', max_length=100),
        ),
        migrations.AddField(
            model_name='relacionthc',
            name='endDate',
            field=models.DateField(blank=True, default=datetime.date(2023, 10, 9)),
        ),
        migrations.AddField(
            model_name='relacionthc',
            name='jornada',
            field=models.CharField(default='Diaria', max_length=100),
        ),
        migrations.AddField(
            model_name='relacionthc',
            name='startDate',
            field=models.DateField(blank=True, default=datetime.date(2023, 10, 9)),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='contractType',
            field=models.CharField(choices=[('Contrato Termino Fijo', 'Contrato Termino Fijo'), ('Contrato Prestación de Servicios', 'Contrato Prestación de Servicios'), ('Contrato Tiempo Parcial', 'Contrato Tiempo Parcial'), ('Contrato a Termino Indefinido', 'Contrato a Termino Indefinido'), ('Contrato Practicante', 'Contrato Practicante')], max_length=100),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='modalidad',
            field=models.CharField(choices=[('Presencial', 'Presencial'), ('Remoto', 'Remoto'), ('Mixto', 'Mixto')], max_length=100),
        ),
    ]