# Generated by Django 4.2.5 on 2023-10-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_relacionthc_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionthc',
            name='contractsObject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='functions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='relacionthc',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
