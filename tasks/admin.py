from django.contrib import admin
from .models import Task, Usuario, TalentoHumano, RelacionTHC, Comentario, Archivo, Correspondencia, Inventario, Observacion, Sede, Foto, Visita

"""
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

"""
admin.site.register(Task) 
admin.site.register(Usuario)
admin.site.register(TalentoHumano)
admin.site.register(RelacionTHC)
admin.site.register(Comentario)
admin.site.register(Archivo)
admin.site.register(Correspondencia)
admin.site.register(Inventario)
admin.site.register(Observacion)
admin.site.register(Sede)
admin.site.register(Foto)
admin.site.register(Visita)
