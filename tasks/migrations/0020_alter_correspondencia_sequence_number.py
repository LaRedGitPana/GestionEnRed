# Generated by Django 4.2.5 on 2023-10-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_alter_correspondencia_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='sequence_number',
            field=models.PositiveIntegerField(),
        ),
    ]