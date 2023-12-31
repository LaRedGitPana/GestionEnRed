# Generated by Django 4.2.5 on 2023-11-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0045_rename_cede_sede'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='lat1',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lat2',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lat3',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon1',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon2',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon3',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
