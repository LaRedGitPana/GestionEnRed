# Generated by Django 4.2.5 on 2023-10-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='file',
            field=models.FileField(blank=True, upload_to=None),
        ),
    ]
