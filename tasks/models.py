from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
import os

today = datetime.date.today()

# Create your models here.

def get_coso_upload_path(instance, filename):
    return os.path.join('tasks', instance.document, filename)

class Task(models.Model):

    CONTRACT_TYPES = [
        ('Contrato', 'Contrato'),
        ('Convenio', 'Convenio'),
        ('Otro', 'Otro')
    ]

    talentohumanos = models.ManyToManyField('TalentoHumano', through='RelacionTHC')

    year = models.PositiveBigIntegerField(default=today.year)
    contractType = models.CharField(max_length=100, choices=CONTRACT_TYPES)
    nombre = models.CharField(max_length=100)
    minimumSalary = models.DecimalField(max_digits=14, decimal_places=2)
    contractValueSMMLV = models.DecimalField(max_digits=14, decimal_places=2)
    contractorsBudget = models.DecimalField(max_digits=14, decimal_places=2)
    redsBudget = models.DecimalField(max_digits=14, decimal_places=2)

    # Calculate totalValue by adding contractorsBudget and redsBudget
    @property
    def totalValue(self):
        return self.contractorsBudget + self.redsBudget
    
    startDate = models.DateField(blank=True)
    endDate = models.DateField(null=True, blank=True)

    # Calculate both durations
    @property
    def durationMonths(self):
        if self.startDate and self.endDate:
            delta = self.endDate - self.startDate
            return delta.days // 30
        return None
    
    @property
    def durationDays(self):
        if self.startDate and self.endDate:
            delta = self.endDate - self.startDate
            return delta.days 
        return None
    
    secop = models.CharField(max_length=100)
    rup = models.CharField(max_length=100)
    document = models.CharField(max_length=100, unique=True)
    contractor = models.CharField(max_length=100)
    departments = models.TextField(blank=True)
    municipalities = models.TextField(blank=True)
    topic = models.CharField(max_length=100)
    object = models.TextField(blank=True)
    resultsIndicator = models.FileField(upload_to=get_coso_upload_path, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.document 

def get_task_upload_path(instance, filename):

    task_document = instance.task.document

    return os.path.join('tasks', task_document, filename)

class Archivo(models.Model):
     
    task = models.ForeignKey(Task, related_name="archivos", on_delete=models.CASCADE)

    name = models.CharField(max_length=100) 
    file = models.FileField(upload_to=get_task_upload_path, blank=True, null=True)
    
    def __str__(self):
        return self.name   
    
class Usuario(models.Model):
    
    USER_TYPES = [
        ('Admin', 'Admin'),
        ('General', 'General'),
        ('Auxiliar', 'Auxiliar'),
        ('Correspondencia', 'Correspondencia')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def nombreCompleto(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        
    document = models.CharField(max_length=100, unique=True)
    red = models.CharField(max_length=100)
    userType = models.CharField(max_length=100, choices=USER_TYPES)

    def __str__(self):
        return str(self.user)
    
def get_talentohumano_upload_path(instance, filename):

    talentohumano_document = instance.document

    return os.path.join('talentohumano', talentohumano_document, filename)

class TalentoHumano(models.Model):

    DOCUMENT_TYPES = [
        ('Cedula de Ciudadania', 'Cedula de Ciudadania'),
        ('Tarjeta de Identidad', 'Tarjeta de Identidad'),
        ('Cedula de Extranjeria', 'Cedula de Extranjeria'),
        ('Pasaporte', 'Pasaporte'),
        ('Registro Civil', 'Registro Civil'),
        ('No. Unico de Id. Personal', 'No. Unico de Id. Personal'),
        ('Per Especial Permanencia', 'Per Especial Permanencia'),
        ('Permiso por Proteccion Temporal', 'Permiso por Proteccion Temporal')
    ]

    SEX_TYPES = [
        ('Mujer', 'Mujer'),
        ('Hombre', 'Hombre'),
        ('Otro', 'Otro')
    ]

    ESCOLARIDAD_TYPES = [
       ('Primaria', 'Primaria'),
       ('Bachillerato', 'Bachillerato'),
       ('Practicante', 'Practicante'),
       ('Pregrado', 'Pregrado'),
       ('Postgrado', 'Postgrado')
    ]

    ESTADOCIVIL_TYPES = [
        ('Soltero(a)', 'Soltero(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viudo(a)', 'Viudo(a)'),
        ('Union Libre', 'Union Libre')
    ]

    CONTRACT_TYPES = [
        ('Contrato Termino Fijo', 'Contrato Termino Fijo'),
        ('Contrato Prestación de Servicios', 'Contrato Prestación de Servicios'),
        ('Contrato Tiempo Parcial', 'Contrato Tiempo Parcial'),
        ('Contrato a Termino Indefinido', 'Contrato a Termino Indefinido'),
        ('Contrato Practicante', 'Contrato Practicante')
    ]

    MODALIDAD_TYPES = [
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Mixto', 'Mixto')
    ]

    activo = models.BooleanField(default=True)
    tasks = models.ManyToManyField('Task', through='RelacionTHC')

    # Personal Window

    idType = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    document = models.CharField(max_length=100, unique=True)
    docExpeditionDate = models.DateField(blank=True)
    expeditionPlace = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100, null=True, blank=True)
    firstLastname = models.CharField(max_length=100)
    secondLastname = models.CharField(max_length=100, null=True, blank=True)

    @property
    def nombreCompleto(self):
        non_null_fields = [self.firstName, self.secondName, self.firstLastname, self.secondLastname]
        return ' '.join(filter(None, non_null_fields))

    sex = models.CharField(max_length=100, choices=SEX_TYPES)
    birthday = models.DateField(blank=True)
    birthPlace = models.CharField(max_length=100)
    residenceAddress = models.CharField(max_length=100)
    municipalitieResidence = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    contactPhone = models.CharField(max_length=20)
    personalEmail = models.EmailField(max_length=254)
    professionalEmail = models.EmailField(max_length=254, null=True)
    escolaridad = models.CharField(max_length=100, choices=ESCOLARIDAD_TYPES)
    profesion = models.CharField(max_length=100, null=True)
    estadoCivil = models.CharField(max_length=100, choices=ESTADOCIVIL_TYPES)
    bloodGroup = models.CharField(max_length=10)

    # SSS Which basically stands for Security and 2 other thingies that start with S

    eps = models.CharField(max_length=100)
    afs = models.CharField(max_length=100)
    codigoCentroTrabajo = models.CharField(max_length=100)
    codigoActividadDesarrollar = models.CharField(max_length=100)

    #Contratación

    contractType = models.CharField(max_length=100, choices=CONTRACT_TYPES)
    modalidad = models.CharField(max_length=100, choices=MODALIDAD_TYPES)
    cargo = models.CharField(max_length=100)
    jornada = models.CharField(max_length=100)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)

    @property
    def durationMonths(self):
        if self.startDate and self.endDate:
            delta = self.endDate - self.startDate
            return delta.days // 30
        return None
        
    monthlySalary = models.DecimalField(max_digits=14, decimal_places=2)
    totalSalary = models.DecimalField(max_digits=14, decimal_places=2)
    functions = models.TextField(blank=True)
    contractsObject = models.TextField(blank=True)
    lugarPrestacionServicios = models.CharField(max_length=100)
    departamentoPrestacionServicios = models.CharField(max_length=100)
    paymentMethod = models.CharField(max_length=100)

    # Soportes 

    drivingLicense = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    titulos = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    disabilityCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    confidentialityCompromise = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    resume = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    idPicture = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    updatedRut = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    libretaMilitar = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    professionalCard = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    medicalCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    vpnCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    treatmentAuthorization = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    laborCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    sexualFormat = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)
    audioPhotoAuthorization = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True)

    def __str__(self):
        return self.document
    
class Comentario(models.Model):

    talentohumano = models.ForeignKey(TalentoHumano, related_name="comments", on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    body = models.TextField()
    date_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.talentohumano.nombreCompleto, self.usuario.nombreCompleto)
    
class RelacionTHC(models.Model):

    CONTRACT_TYPES = [
        ('Contrato Termino Fijo', 'Contrato Termino Fijo'),
        ('Contrato Prestación de Servicios', 'Contrato Prestación de Servicios'),
        ('Contrato Tiempo Parcial', 'Contrato Tiempo Parcial'),
        ('Contrato a Termino Indefinido', 'Contrato a Termino Indefinido'),
        ('Contrato Practicante', 'Contrato Practicante')
    ]

    MODALIDAD_TYPES = [
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Mixto', 'Mixto')
    ]

    talentoHumano = models.ForeignKey(TalentoHumano, on_delete=models.CASCADE)      
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    contractType = models.CharField(max_length=100, choices=CONTRACT_TYPES, null=True)
    modalidad = models.CharField(max_length=100, choices=MODALIDAD_TYPES, null=True)
    cargo = models.CharField(max_length=100, null=True)
    jornada = models.CharField(max_length=100, null=True)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)

    @property
    def durationMonths(self):
        if self.startDate and self.endDate:
            delta = self.endDate - self.startDate
            return delta.days // 30
        return None
    
    monthlySalary = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    totalSalary = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    functions = models.TextField(null=True)
    contractsObject = models.TextField(null=True)
    lugarPrestacionServicios = models.CharField(max_length=100, null=True)
    departamentoPrestacionServicios = models.CharField(max_length=100, null=True)
    paymentMethod = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.talentoHumano) + '/' + str(self.task)
    
def get_correspondencia_upload_path(instance, filename):

    correspondencia_codigo = instance.codigo

    return os.path.join('correspondencia', correspondencia_codigo, filename)
    
class Correspondencia(models.Model):

    CORRESPONDECIA_TYPES = [
        ('Externa', 'Externa'),
        ('Interna', 'Interna')
    ]

    año = models.PositiveBigIntegerField(default=today.year)
    sequence_number_int = models.PositiveIntegerField(null=True)
    sequence_number_ext = models.PositiveIntegerField(null=True)
    codigo = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=100, choices=CORRESPONDECIA_TYPES, null=True)
    dateCreated = models.DateField(blank=True)
    sentTo = models.CharField(max_length=100)
    areaProject = models.CharField(max_length=100)
    asunto = models.TextField()
    document = models.FileField(upload_to=get_correspondencia_upload_path, null=False) 

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo
