# Generated by Django 4.2.5 on 2023-10-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_relacionthc_contractsobject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionthc',
            name='cargo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='contractType',
            field=models.CharField(choices=[('Contrato Termino Fijo', 'Contrato Termino Fijo'), ('Contrato Prestación de Servicios', 'Contrato Prestación de Servicios'), ('Contrato Tiempo Parcial', 'Contrato Tiempo Parcial'), ('Contrato a Termino Indefinido', 'Contrato a Termino Indefinido'), ('Contrato Practicante', 'Contrato Practicante')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='contractsObject',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='departamentoPrestacionServicios',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='functions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='jornada',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='lugarPrestacionServicios',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='modalidad',
            field=models.CharField(choices=[('Presencial', 'Presencial'), ('Remoto', 'Remoto'), ('Mixto', 'Mixto')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='monthlySalary',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='paymentMethod',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='totalSalary',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]
