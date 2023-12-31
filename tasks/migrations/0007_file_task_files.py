# Generated by Django 4.2.5 on 2023-10-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_relacionthc_contractsobject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to=None)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='files',
            field=models.ManyToManyField(related_name='tasks', to='tasks.file'),
        ),
    ]
