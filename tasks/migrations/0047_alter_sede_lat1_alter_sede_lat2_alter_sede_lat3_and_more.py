# Generated by Django 4.2.5 on 2023-11-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0046_alter_sede_lat1_alter_sede_lat2_alter_sede_lat3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='lat1',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lat2',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lat3',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon1',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon2',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sede',
            name='lon3',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
