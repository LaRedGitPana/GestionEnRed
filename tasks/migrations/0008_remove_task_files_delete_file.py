# Generated by Django 4.2.5 on 2023-10-17 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_file_task_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='files',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]