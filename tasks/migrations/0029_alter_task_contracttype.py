# Generated by Django 4.2.5 on 2023-11-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0028_alter_task_contracttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='contractType',
            field=models.CharField(choices=[('Contrato', 'Contrato'), ('Convenio', 'Convenio'), ('Otro', 'Otro')], max_length=100),
        ),
    ]
