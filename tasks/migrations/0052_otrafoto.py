# Generated by Django 4.2.5 on 2023-11-24 15:58

from django.db import migrations, models
import django.db.models.deletion
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0051_alter_visita_observaciongeneral_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtraFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('file', models.ImageField(blank=True, null=True, upload_to=tasks.models.get_visita_upload_path)),
                ('visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='tasks.visita')),
            ],
        ),
    ]