from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
import os

today = datetime.date.today()

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
        return self.document + ' ' + '(' + self.nombre + ')'

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
    titulos = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    disabilityCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    confidentialityCompromise = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    resume = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    idPicture = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    updatedRut = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    libretaMilitar = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    professionalCard = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254, null=True, blank=True) #Este si
    medicalCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    vpnCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    treatmentAuthorization = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    laborCertificate = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    sexualFormat = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)
    audioPhotoAuthorization = models.FileField(upload_to=get_talentohumano_upload_path, max_length=254)

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
    
    class Meta:
        unique_together = ('talentoHumano', 'task')
    
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
    
class Inventario(models.Model):

    ESTADOS_TYPES = [
        ("Bueno", "Bueno"),
        ("Regular", "Regular"),
        ("Averiado/Dañado", "Averiado/Dañado")
    ]

    name = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    caracteristicas = models.TextField()
    codigo = models.CharField(max_length=100)
    serial_num = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, choices=ESTADOS_TYPES) 
    dateAdquired = models.DateField(blank=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    entregadoA = models.CharField(max_length=100, null=True, blank=True)
    redProject = models.CharField(max_length=100, null=True, blank=True)
    dateTaken = models.DateField(blank=True, null=True)
    dateGivenBack = models.DateField(null=True, blank=True)
    prestado = models.BooleanField()

    def __str__(self):
        return self.codigo
    
class Observacion(models.Model):

    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)

    observacion = models.TextField(null=True)
    entregadoA = models.CharField(max_length=100, null=True, blank=True)
    redProject = models.CharField(max_length=100, null=True, blank=True)
    dateTaken = models.DateField()
    dateGivenBack = models.DateField()

    def __str__(self):
        return self.inventario.name + " - " + self.entregadoA + " - " + str(self.dateGivenBack)

class Sede(models.Model):

    LATITUD = [
            ("S", "S"),
            ("N", "N")
    ]

    LONGITUD = [
            ("E", "E"),
            ("O", "O")
    ]
    
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100, choices=LATITUD)
    longitud = models.CharField(max_length=100, choices=LONGITUD) 
    lat1 = models.DecimalField(max_digits=5, decimal_places=2)
    lat2 = models.DecimalField(max_digits=5, decimal_places=2)
    lat3 = models.DecimalField(max_digits=5, decimal_places=2)
    lon1 = models.DecimalField(max_digits=5, decimal_places=2)
    lon2 = models.DecimalField(max_digits=5, decimal_places=2)
    lon3 = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True)

    contrato = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):  
        return self.nombre

class Visita(models.Model):

    OPCIONES = [
        ("SI", "SI"),
        ("NO", "NO"),
        ("N.A.", "N.A.")
    ]

    ESTADO_TYPES = [
        ("Completada","Completada"),
        ("Pendiente","Pendiente")
    ]

    date = models.DateField(blank=True)
    hora = models.TimeField(blank=True)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100, choices=ESTADO_TYPES)

    campo_1_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_1 = models.TextField(null=True, blank=True)
    campo_1_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_2 = models.TextField(null=True, blank=True)
    campo_1_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_3 = models.TextField(null=True, blank=True)
    campo_1_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_4 = models.TextField(null=True, blank=True)
    campo_1_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_5 = models.TextField(null=True, blank=True)
    campo_1_6 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_6 = models.TextField(null=True, blank=True)
    campo_1_7 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_1_7 = models.TextField(null=True, blank=True)
    campo_2_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_1 = models.TextField(null=True, blank=True)
    campo_2_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_2 = models.TextField(null=True, blank=True)
    campo_2_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_3 = models.TextField(null=True, blank=True)
    campo_2_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_4 = models.TextField(null=True, blank=True)
    campo_2_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_5 = models.TextField(null=True, blank=True)
    campo_2_6 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_6 = models.TextField(null=True, blank=True)
    campo_2_7 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_7 = models.TextField(null=True, blank=True)
    campo_2_8 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_8 = models.TextField(null=True, blank=True)
    campo_2_9 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_2_9 = models.TextField(null=True, blank=True)
    campo_3_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_1 = models.TextField(null=True, blank=True)
    campo_3_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_2 = models.TextField(null=True, blank=True)
    campo_3_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_3 = models.TextField(null=True, blank=True)
    campo_3_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_4 = models.TextField(null=True, blank=True)
    campo_3_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_5 = models.TextField(null=True, blank=True)
    campo_3_6 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_6 = models.TextField(null=True, blank=True)
    campo_3_7 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_7 = models.TextField(null=True, blank=True)
    campo_3_8 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_3_8 = models.TextField(null=True, blank=True)
    campo_4_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_1 = models.TextField(null=True, blank=True)
    campo_4_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_2 = models.TextField(null=True, blank=True)
    campo_4_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_3 = models.TextField(null=True, blank=True)
    campo_4_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_4 = models.TextField(null=True, blank=True)
    campo_4_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_5 = models.TextField(null=True, blank=True)
    campo_4_6 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_6 = models.TextField(null=True, blank=True)
    campo_4_7 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_7 = models.TextField(null=True, blank=True)
    campo_4_8 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_8 = models.TextField(null=True, blank=True)
    campo_4_9 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_9 = models.TextField(null=True, blank=True)
    campo_4_10 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_10 = models.TextField(null=True, blank=True)
    campo_4_11 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_4_11 = models.TextField(null=True, blank=True)
    campo_5_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_5_1 = models.TextField(null=True, blank=True)
    campo_6_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_6_1 = models.TextField(null=True, blank=True)
    campo_6_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_6_2 = models.TextField(null=True, blank=True)
    campo_6_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_6_3 = models.TextField(null=True, blank=True)
    campo_6_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_6_4 = models.TextField(null=True, blank=True)
    campo_7_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_7_1 = models.TextField(null=True, blank=True)
    campo_7_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_7_2 = models.TextField(null=True, blank=True)
    campo_7_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_7_3 = models.TextField(null=True, blank=True)
    campo_7_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_7_4 = models.TextField(null=True, blank=True)
    campo_8_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_8_1 = models.TextField(null=True, blank=True)
    campo_8_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_8_2 = models.TextField(null=True, blank=True)
    campo_8_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_8_3 = models.TextField(null=True, blank=True)
    campo_8_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_8_4 = models.TextField(null=True, blank=True)
    campo_8_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_8_5 = models.TextField(null=True, blank=True)
    campo_9_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_9_1 = models.TextField(null=True, blank=True)
    campo_9_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_9_2 = models.TextField(null=True, blank=True)
    campo_10_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_10_1 = models.TextField(null=True, blank=True)
    campo_10_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_10_2 = models.TextField(null=True, blank=True)
    campo_10_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_10_3 = models.TextField(null=True, blank=True)
    campo_10_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_10_4 = models.TextField(null=True, blank=True)
    campo_10_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_10_5 = models.TextField(null=True, blank=True)
    campo_11_1 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_1 = models.TextField(null=True, blank=True)
    campo_11_2 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_2 = models.TextField(null=True, blank=True)
    campo_11_3 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_3 = models.TextField(null=True, blank=True)
    campo_11_4 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_4 = models.TextField(null=True, blank=True)
    campo_11_5 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_5 = models.TextField(null=True, blank=True)
    campo_11_6 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_6 = models.TextField(null=True, blank=True)
    campo_11_7 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_7 = models.TextField(null=True, blank=True)
    campo_11_8 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_8 = models.TextField(null=True, blank=True)
    campo_11_9 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_9 = models.TextField(null=True, blank=True)
    campo_11_10 = models.CharField(max_length=10, choices=OPCIONES)
    observacion_11_10 = models.TextField(null=True, blank=True)
    observacionGeneral = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sede.nombre + '/' + self.usuario.user.username + '/' + str(self.date) + '/' + str(self.hora)

def get_sede_upload_path(instance, filename):

    sede_name = instance.sede.nombre

    return os.path.join('sedes', sede_name, filename)

def get_visita_upload_path(instance, filename):

    visita_name = instance.visita.usuario.user.username + '/' + instance.visita.sede.nombre + '/' + instance.visita.date.strftime('%d-%m-%Y')

    return os.path.join('visitas', visita_name, filename)

def get_upload_path(instance, filename):
    if instance.sede:
        return get_sede_upload_path(instance, filename)
    else:
        return get_visita_upload_path(instance, filename)

class Foto(models.Model):
    sede = models.ForeignKey(Sede, related_name="fotos", on_delete=models.CASCADE, null=True)
    visita = models.ForeignKey(Visita, related_name="fotos", on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=100)
    file = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    def __str__(self):
        return self.number 
