# Generated by Django 4.2.5 on 2023-11-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_correspondencia_created_relacionthc_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talentohumano',
            name='sex',
            field=models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], max_length=100),
        ),
    ]
