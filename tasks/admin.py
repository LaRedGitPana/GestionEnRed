from django.contrib import admin
from .models import Task, Usuario, TalentoHumano, RelacionTHC, Comentario, Archivo, Correspondencia

"""
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

"""
admin.site.register(Task) # Aqui habia algo mas era como , TaskAdmin o una vaina asi
admin.site.register(Usuario)
admin.site.register(TalentoHumano)
admin.site.register(RelacionTHC)
admin.site.register(Comentario)
admin.site.register(Archivo)
admin.site.register(Correspondencia)
