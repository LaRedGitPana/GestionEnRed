# Generated by Django 4.2.5 on 2023-10-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_correspondencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='sequence_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
