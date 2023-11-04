"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('task_wizard/<int:step>/',views.task_wizard, name='task_wizard'),
    path('usuarios/', views.usuarios, name='usuarios'), 
    path('usuarios/<int:usuario_id>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/<int:usuario_id>/password_change/', views.password_change, name='password_change'),
    path('usuarios/<int:usuario_id>/delete/', views.delete_usuario, name='delete_usuario'), 
    path('crear_usuario/', views.crear_user, name='crear_usuario'),
    path('talentohumanos/', views.talentohumanos, name='talentohumanos'),
    path('talentohumano_wizard/<int:step>/',views.talentohumano_wizard, name='talentohumano_wizard'), 
    path('talentohumanos/<int:talentohumano_id>/', views.talentohumano_detail, name='talentohumano_detail'),  
    path('talentohumanos/<int:talentohumano_id>/delete/', views.delete_talentohumano, name='delete_talentohumano'),      
    path('asignacion/<int:task_id>', views.asignacion, name='asignacion'),
    path('relaciones/', views.relaciones, name='relaciones'),
    path('relaciones/<int:relacion_id>/', views.relacion_detail, name='relacion_detail'),
    path('relaciones/<int:relacion_id>/delete/', views.delete_relacion, name='delete_relacion'),
    path('generarLaboral/<int:talentohumano_id>/', views.generarLaboral, name='generarLaboral'),
    path('generarOtro/<int:relacion_id>/', views.generarOtro, name="generarOtro"),
    path('talentohumanos/<int:talentohumano_id>/add_comment/', views.add_comment, name='add_comment'),
    path('tasks/<int:task_id>/add_archivo', views.add_archivo, name='add_archivo'),
    path('tasks/report/', views.generate_excel_report_tasks, name='generate_excel_report_tasks'),
    path('talentohumanos/report/', views.generate__excel_report_talentohumanos, name='generate_excel_report_talentohumanos'),
    path('correspondencias/', views.correspondencias, name='correspondencias'),
    path('correspondencias/<int:correspondencia_id>/', views.correspondencia_detail, name='correspondencia_detail'),
    path('correspondencias_int/', views.correspondencias_int, name='correspondencias_int'),
    path('correspondencias_ext/', views.correspondencias_ext, name='correspondencias_ext'),
    path('correspondencias_int/crear/', views.crear_correspondencia_int, name='crear_correspondencia_int'),
    path('correspondencias_ext/crear/', views.crear_correspondencia_ext, name='crear_correspondencia_ext'),
    path('correspondencias/<int:correspondencia_id>/delete/', views.delete_correspondencia, name='delete_correspondencia'),
    path('correspondencias/report/', views.generate__excel_report_correspondencias, name='generate_excel_report_correspondencias')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
