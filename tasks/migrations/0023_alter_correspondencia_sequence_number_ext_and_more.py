# Generated by Django 4.2.5 on 2023-10-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_rename_sequence_number_correspondencia_sequence_number_ext_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='sequence_number_ext',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='sequence_number_int',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
