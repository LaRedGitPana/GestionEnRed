# Generated by Django 4.2.5 on 2023-10-27 14:49

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_alter_correspondencia_sequence_number_ext_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='document',
            field=models.FileField(blank=True, upload_to=tasks.models.get_correspondencia_upload_path),
        ),
    ]
