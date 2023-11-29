# Generated by Django 4.2.5 on 2023-11-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0034_alter_inventario_dateadquired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='dateAdquired',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='dateTaken',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='entregadoA',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='estado',
            field=models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Averiado/Dañado', 'Averiado/Dañado')], max_length=100),
        ),
    ]
