# Generated by Django 4.2.5 on 2023-11-22 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0042_alter_observaciones_observacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Observaciones',
            new_name='Observacion',
        ),
    ]