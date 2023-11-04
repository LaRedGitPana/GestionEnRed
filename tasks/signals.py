from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from tasks.models import Task

@receiver(pre_delete, sender=Task)
def delete_related_files(sender, instance, **kwargs):
    for archivo in instance.archivos.all():
        if archivo.file:
            if os.path.isfile(archivo.file.path):
                os.remove(archivo.file.path)
        archivo.delete()