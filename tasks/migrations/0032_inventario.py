# Generated by Django 4.2.5 on 2023-11-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_alter_task_resultsindicator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]