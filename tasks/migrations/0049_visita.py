# Generated by Django 4.2.5 on 2023-11-23 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0048_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('hora', models.TimeField(blank=True)),
                ('departamento', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('campo_1_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_1', models.TextField(null=True)),
                ('campo_1_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_2', models.TextField(null=True)),
                ('campo_1_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_3', models.TextField(null=True)),
                ('campo_1_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_4', models.TextField(null=True)),
                ('campo_1_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_5', models.TextField(null=True)),
                ('campo_1_6', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_6', models.TextField(null=True)),
                ('campo_1_7', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_1_7', models.TextField(null=True)),
                ('campo_2_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_1', models.TextField(null=True)),
                ('campo_2_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_2', models.TextField(null=True)),
                ('campo_2_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_3', models.TextField(null=True)),
                ('campo_2_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_4', models.TextField(null=True)),
                ('campo_2_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_5', models.TextField(null=True)),
                ('campo_2_6', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_6', models.TextField(null=True)),
                ('campo_2_7', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_7', models.TextField(null=True)),
                ('campo_2_8', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_8', models.TextField(null=True)),
                ('campo_2_9', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_2_9', models.TextField(null=True)),
                ('campo_3_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_1', models.TextField(null=True)),
                ('campo_3_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_2', models.TextField(null=True)),
                ('campo_3_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_3', models.TextField(null=True)),
                ('campo_3_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_4', models.TextField(null=True)),
                ('campo_3_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_5', models.TextField(null=True)),
                ('campo_3_6', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_6', models.TextField(null=True)),
                ('campo_3_7', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_7', models.TextField(null=True)),
                ('campo_3_8', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_3_8', models.TextField(null=True)),
                ('campo_4_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_1', models.TextField(null=True)),
                ('campo_4_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_2', models.TextField(null=True)),
                ('campo_4_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_3', models.TextField(null=True)),
                ('campo_4_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_4', models.TextField(null=True)),
                ('campo_4_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_5', models.TextField(null=True)),
                ('campo_4_6', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_6', models.TextField(null=True)),
                ('campo_4_7', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_7', models.TextField(null=True)),
                ('campo_4_8', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_8', models.TextField(null=True)),
                ('campo_4_9', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_9', models.TextField(null=True)),
                ('campo_4_10', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_10', models.TextField(null=True)),
                ('campo_4_11', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_4_11', models.TextField(null=True)),
                ('campo_5_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_5_1', models.TextField(null=True)),
                ('campo_6_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_6_1', models.TextField(null=True)),
                ('campo_6_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_6_2', models.TextField(null=True)),
                ('campo_6_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_6_3', models.TextField(null=True)),
                ('campo_6_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_6_4', models.TextField(null=True)),
                ('campo_7_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_7_1', models.TextField(null=True)),
                ('campo_7_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_7_2', models.TextField(null=True)),
                ('campo_7_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_7_3', models.TextField(null=True)),
                ('campo_7_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_7_4', models.TextField(null=True)),
                ('campo_8_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_8_1', models.TextField(null=True)),
                ('campo_8_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_8_2', models.TextField(null=True)),
                ('campo_8_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_8_3', models.TextField(null=True)),
                ('campo_8_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_8_4', models.TextField(null=True)),
                ('campo_8_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_8_5', models.TextField(null=True)),
                ('campo_9_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_9_1', models.TextField(null=True)),
                ('campo_9_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_9_2', models.TextField(null=True)),
                ('campo_10_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_10_1', models.TextField(null=True)),
                ('campo_10_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_10_2', models.TextField(null=True)),
                ('campo_10_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_10_3', models.TextField(null=True)),
                ('campo_10_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_10_4', models.TextField(null=True)),
                ('campo_10_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_10_5', models.TextField(null=True)),
                ('campo_11_1', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_1', models.TextField(null=True)),
                ('campo_11_2', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_2', models.TextField(null=True)),
                ('campo_11_3', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_3', models.TextField(null=True)),
                ('campo_11_4', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_4', models.TextField(null=True)),
                ('campo_11_5', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_5', models.TextField(null=True)),
                ('campo_11_6', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_6', models.TextField(null=True)),
                ('campo_11_7', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_7', models.TextField(null=True)),
                ('campo_11_8', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_8', models.TextField(null=True)),
                ('campo_11_9', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_9', models.TextField(null=True)),
                ('campo_11_10', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('N.A.', 'N.A.')], max_length=10)),
                ('observacion_11_10', models.TextField(null=True)),
                ('observacionGeneral', models.TextField(null=True)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.sede')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.usuario')),
            ],
        ),
    ]
