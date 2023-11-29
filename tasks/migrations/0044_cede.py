# Generated by Django 4.2.5 on 2023-11-22 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0043_rename_observaciones_observacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('latitud', models.CharField(choices=[('S', 'S'), ('N', 'N')], max_length=100)),
                ('longitud', models.CharField(choices=[('E', 'E'), ('O', 'O')], max_length=100)),
                ('lat1', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lat2', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lat3', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lon1', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lon2', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lon3', models.DecimalField(decimal_places=2, max_digits=2)),
                ('descripcion', models.TextField(blank=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
