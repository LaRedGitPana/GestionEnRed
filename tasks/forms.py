from django import forms
from .models import Task, Usuario, TalentoHumano, RelacionTHC, Comentario, Archivo, Correspondencia, Inventario, Observacion, Sede, Foto, Visita
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
import datetime
from django.utils.safestring import mark_safe

today = datetime.date.today()
YEAR_CHOICES = [tuple([x,x]) for x in range(1900, today.year + 2)]

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['year', 'contractType', 'nombre', 'minimumSalary', 'contractValueSMMLV', 'contractorsBudget', 'redsBudget', 'startDate', 'endDate', 'secop', 'rup', 'document', 'contractor', 'topic', 'object', 'resultsIndicator', 'departments', 'municipalities'] 
        widgets = {
            'year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control'}),
            'contractType': forms.Select(choices=Task.CONTRACT_TYPES, attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del contrato'}),
            'minimumSalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario minimo'}),
            'contractValueSMMLV': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor del contrato en SMMLV'}),
            'contractorsBudget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el aporte del contratante'}),
            'redsBudget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el aporte del la RED'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'secop': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce the secop'}),
            'rup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce the rup'}),
            'document': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your document'}),
            'contractor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the name of your contractor'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the topic'}),
            'object': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the object', 'rows': 5, 'cols': 40}),
            'resultsIndicator': forms.FileInput(attrs={'class': 'form-control'}),
            'departments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the name of the pertinent departments'}),
            'municipalities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the name of the pertinent municipalities'})
        }
        labels = {
            'year': 'Año',
            'contractType': 'Tipo de Contrato',
            'nombre': 'Nombre del Contrato',
            'minimumSalary': 'Salario Minimo',
            'contractValueSMMLV': 'Valor Contrato en SMMLV',
            'contractorsBudget': 'Aporte Contratante',
            'redsBudget': 'Aporte Fundación ONG LA RED',    
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Terminación',
            'secop': 'Secop',
            'rup': 'Rup',
            'document': 'Documento',
            'contractor': 'Contratante',
            'topic': 'Tema',
            'object': 'Objeto',
            'resultsIndicator': 'Indicadores de Resultados',
            'departments': 'Departamentos',
            'municipalities': 'Municipios'  
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

        return cleaned_data

class TaskFormPart1(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['year', 'startDate', 'endDate']
        widgets = {
            'year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'year': 'Año',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Terminación',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

        return cleaned_data

class TaskFormPart2(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['minimumSalary', 'contractValueSMMLV', 'contractorsBudget', 'redsBudget']
        widgets = {
            'minimumSalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario minimo'}),
            'contractValueSMMLV': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor del contrato en SMMLV'}),
            'contractorsBudget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el aporte del contratante'}),
            'redsBudget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el aporte de la Fundación ONG LA RED'}),            
        }
        labels = {
            'minimumSalary': 'Salario Minimo',
            'contractValueSMMLV': 'Valor Contrato en SMMLV',
            'contractorsBudget': 'Aporte Contratante',
            'redsBudget': 'Aporte Fundación ONG LA RED',       
        }

class TaskFormPart3(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['contractType', 'nombre', 'secop', 'rup', 'document', 'contractor', 'topic', 'object', 'resultsIndicator', 'departments', 'municipalities']
        widgets = {
            'contractType': forms.Select(choices=Task.CONTRACT_TYPES, attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del contrato'}),
            'secop': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el secop'}),
            'rup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el rup'}),
            'document': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el identificador del contrato'}),
            'contractor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del contratante'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tema'}),
            'object': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese las funciones especificas', 'rows': 5, 'cols': 40}),
            'resultsIndicator': forms.FileInput(attrs={'class': 'form-control'}),
            'departments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de los departamentos'}),
            'municipalities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de los municipios'})            
        }
        labels = {
            'contractType': 'Tipo de Contrato',
            'nombre': 'Nombre del Contrato',
            'secop': '# Secop',
            'rup': '# RUP',
            'document': 'Documento',
            'contractor': 'Contratante',
            'topic': 'Tema',
            'object': 'Objeto',
            'resultsIndicator': 'Indicadores de Resultados',
            'departments': 'Departamentos',
            'municipalities': 'Municipios'    
        }

class ArchivoForm(forms.ModelForm):

    class Meta:
        model = Archivo
        fields = ['name', 'file']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del archivo'}),
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Nombre del Archivo',
            'file': 'Archivo'
        }

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        super(ArchivoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ArchivoForm, self).save(commit=False)
        if self.task:
            instance.task = self.task
        if commit:
            instance.save()
        return instance


class UsuarioForm(UserCreationForm):
    username = forms.CharField(label = 'Nombre de Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de Usuario'}))
    first_name = forms.CharField(label = 'Primer Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus nombres'}))
    last_name = forms.CharField( label = 'Primer Apellido', max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese sus apellidos'}))    
    password1 = forms.CharField(label = 'Contraseña', max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}))
    password2 = forms.CharField(label = 'Confirmar Contraseña', max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme la contraseña'}))
    document = forms.CharField(label = 'Documento de Identidad', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su documento'}))
    red = forms.CharField(label = 'Red a la que pertenece', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la red o proyecto'}))
    userType = forms.ChoiceField(label = 'Tipo de Usuario', choices=Usuario.USER_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        
        usuario = Usuario(
            user=user,
            document=self.cleaned_data['document'],
            red=self.cleaned_data['red'],
            userType=self.cleaned_data['userType']
        )
        usuario.save()

        return user
    
class AdminEditForm(forms.ModelForm):
    username = forms.CharField(label = 'Nombre de Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de Usuario'}))
    first_name = forms.CharField(label = 'Primer Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus nombres'}))
    last_name = forms.CharField( label = 'Primer Apellido', max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese sus apellidos'}))    
    password1 = forms.CharField(label = 'Contraseña', max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}))
    password2 = forms.CharField(label = 'Confirmar Contraseña', max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme la contraseña'}))
    document = forms.CharField(label = 'Documento', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su documento'}))
    red = forms.CharField(label = 'Red a la que pertenece', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la red o proyecto'}))
    userType = forms.ChoiceField(label = 'Tipo de Usuario', choices=Usuario.USER_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'document', 'red', 'userType']

    def __init__(self, *args, **kwargs):
        super(AdminEditForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        if self.instance:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['document'].initial = self.instance.document
            self.fields['red'].initial = self.instance.red
            self.fields['userType'].initial = self.instance.userType

    def save(self, commit=True):
        usuario = self.instance
        usuario.username = self.cleaned_data['username']
        usuario.first_name = self.cleaned_data['first_name']
        usuario.last_name = self.cleaned_data['last_name']
        usuario.document = self.cleaned_data['document']
        usuario.red = self.cleaned_data['red']
        usuario.userType = self.cleaned_data['userType']

        if commit:
            usuario.save()
            usuario.user.save()

        return usuario
    
class CustomPasswordForm (PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña antigua'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la nueva contraseña'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme la nueva contraseña'})

        self.fields['old_password'].label = mark_safe('<b>Contraseña Antigua</b>')
        self.fields['new_password1'].label = mark_safe('<b>Nueva Contraseña</b>')
        self.fields['new_password2'].label = mark_safe('<b>Confirmar nueva Contraseña</b>') 

        self.error_messages = {
            'password_incorrect': 'Su contraseña antigua fue ingresada incorrectamente, por favor vuelve a intentarlo',
            'password_mismatch': 'Las 2 contraseñas no son iguales, por favor vuelve a intentarlo.',
        }   

class UsuarioEditForm(forms.ModelForm):

    document = forms.CharField(label = 'Documento', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su documento'}))
    red = forms.CharField(label = 'Red a la que pertenece', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la red a la que pertenece'}))
    userType = forms.ChoiceField(label = 'Tipo de Usuario', choices=Usuario.USER_TYPES, widget=forms.Select(attrs={'class': 'form-control'})) 

    class Meta:
        model = Usuario
        fields = ['document', 'red', 'userType']

        def save(self, commit=True):
            usuario = super().save(commit=False)
            if commit:
                usuario.save()
            return usuario
        
class UserEditForm(forms.ModelForm):

    username = forms.CharField(label = 'Nombre de Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de Usuario'}))
    first_name = forms.CharField(label = 'Primer Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su primer nombre'}))
    last_name = forms.CharField( label = 'Primer Apellido', max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese su primer apellido'})) 
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user

class TalentoHumanoForm(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = ['activo', 'idType', 'document', 'docExpeditionDate', 'expeditionPlace', 'firstName', 'secondName', 'firstLastname', 'secondLastname', 'sex', 'birthday', 'birthPlace', 'residenceAddress', 'municipalitieResidence', 'phone', 'contactPhone', 'personalEmail', 'professionalEmail', 'escolaridad', 'profesion', 'estadoCivil', 'bloodGroup', 'eps', 'afs', 'codigoCentroTrabajo', 'codigoActividadDesarrollar', 'contractType', 'modalidad', 'cargo', 'jornada', 'startDate', 'endDate', 'monthlySalary', 'totalSalary', 'functions', 'contractsObject', 'lugarPrestacionServicios', 'departamentoPrestacionServicios', 'paymentMethod', 'drivingLicense', 'titulos', 'disabilityCertificate', 'confidentialityCompromise', 'resume', 'idPicture', 'updatedRut', 'libretaMilitar', 'professionalCard', 'medicalCertificate', 'vpnCertificate', 'treatmentAuthorization', 'laborCertificate', 'sexualFormat', 'audioPhotoAuthorization']
        widgets = {
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idType': forms.Select(choices=TalentoHumano.DOCUMENT_TYPES, attrs={'class': 'form-control'}),
            'document': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su documento'}),
            'docExpeditionDate': forms.DateInput(attrs={'type': 'date'}),
            'expeditionPlace': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el lugar de expedicion del documento'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su primer nombre'}),
            'secondName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su segundo nombre'}),
            'firstLastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su primer apellido'}),
            'secondLastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su segundo apellido'}),
            'sex': forms.Select(choices=TalentoHumano.SEX_TYPES, attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'birthPlace': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su lugar de nacimiento'}),
            'residenceAddress': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su dirección de residencia'}),
            'municipalitieResidence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el municipio donde reside'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su numero de telefono'}),
            'contactPhone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese numero de telefono de su contacto'}),
            'personalEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo personal'}),
            'professionalEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo institucional'}),
            'escolaridad': forms.Select(choices=TalentoHumano.ESCOLARIDAD_TYPES, attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su profesion'}),
            'estadoCivil': forms.Select(choices=TalentoHumano.ESTADOCIVIL_TYPES, attrs={'class': 'form-control'}),
            'bloodGroup': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su grupo sanguineo'}),
            'eps': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la eps a la que esta afiliado(a)'}),
            'afs': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la afs a la que esta afiliado(a)'}),
            'codigoCentroTrabajo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el codigo del centro de trabajo'}),
            'codigoActividadDesarrollar': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el codigo de actividad a desarrollar'}),
            'contractType': forms.Select(choices=TalentoHumano.CONTRACT_TYPES, attrs={'class': 'form-control'}),
            'modalidad': forms.Select(choices=TalentoHumano.MODALIDAD_TYPES, attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su cargo'}),
            'jornada': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su jornada laboral'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'monthlySalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario mensual'}),
            'totalSalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario total'}),
            'functions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Actividades Especificas', 'rows': 5, 'cols': 40}),
            'contractsObject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Objeto del contrato', 'rows': 5, 'cols': 40}),
            'lugarPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el lugar de prestación de servicios'}),
            'departamentoPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el departamento de prestación de servicios'}),
            'paymentMethod': forms.TextInput(attrs={'class': 'form-control'}),
            'drivingLicense': forms.FileInput(attrs={'class': 'form-control'}),
            'titulos': forms.FileInput(attrs={'class': 'form-control'}),
            'disabilityCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'confidentialityCompromise': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'idPicture': forms.FileInput(attrs={'class': 'form-control'}),
            'updatedRut': forms.FileInput(attrs={'class': 'form-control'}),
            'libretaMilitar': forms.FileInput(attrs={'class': 'form-control'}),
            'professionalCard': forms.FileInput(attrs={'class': 'form-control'}),
            'medicalCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'vpnCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'treatmentAuthorization': forms.FileInput(attrs={'class': 'form-control'}),
            'laborCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'sexualFormat': forms.FileInput(attrs={'class': 'form-control'}),
            'audioPhotoAuthorization': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'activo': 'Activo',
            'idType': 'Tipo de Identificación',
            'document': 'Documento',
            'docExpeditionDate': 'Fecha de Expedición del Documento',
            'expeditionPlace': 'Lugar de Expedición del Documento',
            'firstName': 'Primer Nombre',
            'secondName': 'Segundo Nombre',
            'firstLastname': 'Primer Apellido',
            'secondLastname': 'Segundo Apellido',
            'sex': 'Sexo',
            'birthday': 'Fecha de Nacimiento',
            'birthPlace': 'Lugar de Nacimiento',
            'residenceAddress': 'Dirección',
            'municipalitieResidence': 'Municipio de Residencia',
            'phone': 'Telefono',
            'contactPhone': 'Telefono del Contacto',
            'personalEmail': 'Correo Personal',
            'professionalEmail': 'Correo Institucional',
            'escolaridad': 'Escolaridad',
            'profesion': 'Profesión',
            'estadoCivil': 'Estado Civil',
            'bloodGroup': 'Grupo Sanguineo',
            'eps': 'EPS',
            'afs': 'AFS',
            'codigoCentroTrabajo': 'Codigo del Centro de Trabajo',
            'codigoActividadDesarrollar': 'Codigo de la Actividad a Desarrollar', 
            'contractType': 'Tipo de Contrato',
            'modalidad': 'Modalidad de Trabajo',
            'cargo': 'Cargo',
            'jornada': 'Jornada Laboral',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Terminación',
            'monthlySalary': 'Salario Mensual',
            'totalSalary': 'Salario Total',
            'functions': 'Funciones Especificas',
            'contractsObject': 'Objeto del Contrato',
            'lugarPrestacionServicios': 'Lugar de Prestación de Servicios',
            'departamentoPrestacionServicios': 'Departamento de Prestación de Servicios',
            'paymentMethod': 'Metodo de Pago',
            'drivingLicense': 'Licencia de Conducir',
            'titulos': 'Titulos',
            'disabilityCertificate': 'Certificado de Discapacidad',
            'confidentialityCompromise': 'Compromiso de Confidencialidad',
            'resume': 'Hoja de Vida',
            'idPicture': 'Foto del Documento de Identidad',
            'updatedRut': 'RUT Actualizado',
            'libretaMilitar': 'Libreta Militar',
            'professionalCard': 'Carta Profesional',
            'medicalCertificate': 'Certificado Medico',
            'vpnCertificate': 'Certificado VPN',
            'treatmentAuthorization': 'Autorización de Tratamiento de Datos',
            'laborCertificate': 'Certificado Laboral',
            'sexualFormat': 'Formato Consulta Delitos Sexuales',
            'audioPhotoAuthorization': 'Autorización de uso de Audio, Foto y Video'            
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

        return cleaned_data

class TalentoHumanoFormPart1(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = ['activo', 'idType', 'document', 'docExpeditionDate', 'expeditionPlace', 'firstName', 'secondName', 'firstLastname', 'secondLastname', 'sex', 'birthday', 'birthPlace', 'residenceAddress', 'municipalitieResidence', 'phone', 'contactPhone', 'personalEmail', 'professionalEmail', 'escolaridad', 'profesion', 'estadoCivil', 'bloodGroup']
        widgets = {
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idType': forms.Select(choices=TalentoHumano.DOCUMENT_TYPES, attrs={'class': 'form-control'}),
            'document': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su documento'}),
            'docExpeditionDate': forms.DateInput(attrs={'type': 'date'}),
            'expeditionPlace': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el lugar de expedicion del documento'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su primer nombre'}),
            'secondName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su segundo nombre'}),
            'firstLastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su primer apellido'}),
            'secondLastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su segundo apellido'}),
            'sex': forms.Select(choices=TalentoHumano.SEX_TYPES, attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'birthPlace': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su lugar de nacimiento'}),
            'residenceAddress': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su dirección de residencia'}),
            'municipalitieResidence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el municipio donde reside'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su numero de telefono'}),
            'contactPhone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese numero de telefono de su contacto'}),
            'personalEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo personal'}),
            'professionalEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo institucional'}),
            'escolaridad': forms.Select(choices=TalentoHumano.ESCOLARIDAD_TYPES, attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su profesion'}),
            'estadoCivil': forms.Select(choices=TalentoHumano.ESTADOCIVIL_TYPES, attrs={'class': 'form-control'}),
            'bloodGroup': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su grupo sanguineo'}),
        }
        labels = {
            'activo': 'Talento Humano Activo',
            'idType': 'Tipo de Documento',
            'document': 'Numero de Documento',
            'docExpeditionDate': 'Fecha de Expedición del Documento',
            'expeditionPlace': 'Lugar de Expedición del Documento',
            'firstName': 'Primer Nombre',
            'secondName': 'Segundo Nombre',
            'firstLastname': 'Primer Apellido',
            'secondLastname': 'Segundo Apellido',
            'sex': 'Sexo',
            'birthday': 'Fecha de Nacimiento',
            'birthPlace': 'Lugar de Nacimiento',
            'residenceAddress': 'Dirección',
            'municipalitieResidence': 'Municipio de Residencia',
            'phone': 'Telefono',
            'contactPhone': 'Telefono de un Contacto',
            'personalEmail': 'Correo Personal',
            'professionalEmail': 'Correo Institucional',
            'escolaridad': 'Nivel de Escolaridad',
            'profesion': 'Profesion',
            'estadoCivil': 'Estado Civil',
            'bloodGroup': 'Grupo Sanguineo'
        }

class TalentoHumanoFormPart2(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = ['eps', 'afs', 'codigoCentroTrabajo', 'codigoActividadDesarrollar']
        widgets = {
            'eps': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la eps a la que esta afiliado(a)'}),
            'afs': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la afs a la que esta afiliado(a)'}),
            'codigoCentroTrabajo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el codigo del centro de trabajo'}),
            'codigoActividadDesarrollar': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el codigo de actividad a desarrollar'}),
        }
        labels = {
            'eps': 'EPS',
            'afs': 'AFS',
            'codigoCentroTrabajo': 'Codigo del Centro de Trabajo',
            'codigoActividadDesarrollar': 'Codigo de la Actividad a Desarrollar'
        }

class TalentoHumanoFormPart3(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = ['contractType', 'modalidad', 'cargo', 'jornada', 'startDate', 'endDate', 'monthlySalary', 'totalSalary', 'functions', 'contractsObject', 'lugarPrestacionServicios', 'departamentoPrestacionServicios', 'paymentMethod']
        widgets = {
            'contractType': forms.Select(choices=TalentoHumano.CONTRACT_TYPES, attrs={'class': 'form-control'}),
            'modalidad': forms.Select(choices=TalentoHumano.MODALIDAD_TYPES, attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su cargo'}),
            'jornada': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su jornada laboral'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'monthlySalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor de los honorarios mensuales del CPSP'}),
            'totalSalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor total del CPSP'}),
            'functions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Actividades Especificas', 'rows': 5, 'cols': 40}),
            'contractsObject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Objeto del contrato', 'rows': 5, 'cols': 40}),
            'lugarPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el lugar de prestación de servicios'}),
            'departamentoPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el departamento de prestación de servicios'}),
            'paymentMethod': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el metodo de pago'})
        }
        labels = {
            'contractType': 'Tipo de Contrato',
            'modalidad': 'Modalidad de Trabajo',
            'cargo': 'Cargo',
            'jornada': 'Jornada Laboral',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Terminación',
            'monthlySalary': 'Valor Mensual del CPSP',
            'totalSalary': 'Valor Total del CPSP',
            'functions': 'Actividades Especificas',
            'contractsObject': 'Objeto del Contrato',
            'lugarPrestacionServicios': 'Lugar de Prestación de Servicios',
            'departamentoPrestacionServicios': 'Departamento de Prestación de Servicios',
            'paymentMethod': 'Metodo de Pago'            
        }

    def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("startDate")
            end_date = cleaned_data.get("endDate")

            if start_date and end_date and start_date > end_date:
                raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

            return cleaned_data

class TalentoHumanoFormPart4(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = ['drivingLicense', 'titulos', 'disabilityCertificate', 'confidentialityCompromise', 'resume', 'idPicture', 'updatedRut', 'libretaMilitar', 'professionalCard', 'medicalCertificate', 'vpnCertificate', 'treatmentAuthorization', 'laborCertificate', 'sexualFormat', 'audioPhotoAuthorization']
        widgets = {
            'drivingLicense': forms.FileInput(attrs={'class': 'form-control'}),
            'titulos': forms.FileInput(attrs={'class': 'form-control'}),
            'disabilityCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'confidentialityCompromise': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'idPicture': forms.FileInput(attrs={'class': 'form-control'}),
            'updatedRut': forms.FileInput(attrs={'class': 'form-control'}),
            'libretaMilitar': forms.FileInput(attrs={'class': 'form-control'}),
            'professionalCard': forms.FileInput(attrs={'class': 'form-control'}),
            'medicalCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'vpnCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'treatmentAuthorization': forms.FileInput(attrs={'class': 'form-control'}),
            'laborCertificate': forms.FileInput(attrs={'class': 'form-control'}),
            'sexualFormat': forms.FileInput(attrs={'class': 'form-control'}),
            'audioPhotoAuthorization': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'drivingLicense': 'Licencia de Conducción',
            'titulos': 'Titulos',
            'disabilityCertificate': 'Certificado de Discapacidad',
            'confidentialityCompromise': 'Compromiso de Confidencialidad',
            'resume': 'Hoja de Vida',
            'idPicture': 'Documento de Identidad',
            'updatedRut': 'RUT Actualizado',
            'libretaMilitar': 'Libreta Militar',
            'professionalCard': 'Carta Profesional',
            'medicalCertificate': 'Certificado Medico',
            'vpnCertificate': 'Certificado VPN',
            'treatmentAuthorization': 'Autorización de Tratamiento de Datos',
            'laborCertificate': 'Certificado Laboral',
            'sexualFormat': 'Formato Consulta Delitos Sexuales',
            'audioPhotoAuthorization': 'Autorización de uso de Audio, Foto y Video'
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su comentario'})
        }
        labels = {
            'body': 'Comentario'
        }

        def __init__(self, *args, **kwargs):
            self.usuario = kwargs.pop('usuario', None)
            self.talentohumano = kwargs.pop('talentohumano', None)
            super(ComentarioForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            instance = super(ComentarioForm, self).save(commit=False)
            if self.usuario:
                instance.usuario = self.usuario
            if self.talentohumano:
                instance.talentohumano = self.talentohumano
            if commit:
                instance.save()
            return instance

class TalentoHumanoAsignacionForm(forms.Form):
    talentohumanos = forms.ModelMultipleChoiceField(
        queryset=TalentoHumano.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        label='Seleccione el Talento Humano que desea asignar al Contrato'
    )

    def __init__(self, *args, **kwargs):
        super(TalentoHumanoAsignacionForm, self).__init__(*args, **kwargs)
        self.fields['talentohumanos'].queryset = TalentoHumano.objects.filter(activo=True)

        self.fields['talentohumanos'].label_from_instance = lambda obj: f"{obj.document} - {obj.nombreCompleto}"

class RelacionTHCForm(forms.ModelForm):
    class Meta:
        model = RelacionTHC
        fields = ['contractType', 'modalidad', 'cargo', 'jornada', 'startDate', 'endDate', 'monthlySalary', 'totalSalary', 'functions', 'contractsObject', 'lugarPrestacionServicios', 'departamentoPrestacionServicios', 'paymentMethod']
        widgets = {
            'contractType': forms.Select(choices=TalentoHumano.CONTRACT_TYPES, attrs={'class': 'form-control'}),
            'modalidad': forms.Select(choices=TalentoHumano.MODALIDAD_TYPES, attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su cargo'}),
            'jornada': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su jornada laboral'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'monthlySalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor de los honorarios mensuales del CPSP'}),
            'totalSalary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor total del CPSP'}),
            'functions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Actividades Especificas','rows': 5, 'cols': 40}),
            'contractsObject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Objeto del contrato', 'rows': 5, 'cols': 40}),
            'lugarPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el lugar de prestación de servicios'}),
            'departamentoPrestacionServicios': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el departamento de prestación de servicios'}),
            'paymentMethod': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el metodo de pago'})
        }
        labels = {
            'contractType': 'Tipo de Contrato',
            'modalidad': 'Modalidad de Trabajo',
            'cargo': 'Cargo',
            'jornada': 'Jornada Laboral',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Terminación',
            'monthlySalary': 'Valor Mensual del CPSP',
            'totalSalary': 'Valor Total del CPSP',
            'functions': 'Actividades Especificas',
            'contractsObject': 'Objeto del Contrato',
            'lugarPrestacionServicios': 'Lugar de Prestación de Servicios',
            'departamentoPrestacionServicios': 'Departamento de Prestación de Servicios',
            'paymentMethod': 'Metodo de Pago'   
        }

    def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("startDate")
            end_date = cleaned_data.get("endDate")

            if start_date and end_date and start_date > end_date:
                raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

            return cleaned_data

class CorrespondeciaForm(forms.ModelForm):
    class Meta:
        model = Correspondencia
        fields = ['dateCreated', 'areaProject', 'asunto', 'document', 'sentTo']
        widgets = {
            'dateCreated': forms.DateInput(attrs={'type': 'date'}),
            'areaProject': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el area o el proyecto pertinente'}),
            'asunto': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingrese el asunto', 'rows': 2, 'cols': 40}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
            'sentTo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese a que se le envia esta correspondecia'})
        }
        labels = {
            'dateCreated': 'Fecha de Creación',
            'areaProject': 'Area o Proyecto',
            'asunto': 'Asunto',
            'document': 'Archivo',
            'sentTo': 'Enviado a'
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['name', 'cantidad', 'descripcion', 'caracteristicas', 'codigo', 'serial_num', 'marca', 'estado', 'dateAdquired', 'valor', 'entregadoA', 'redProject', 'dateTaken', 'dateGivenBack']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el nombre'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingrese la descripción', 'rows': 2, 'cols': 40}),
            'caracteristicas': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingrese las caracteristicas', 'rows': 2, 'cols': 40}),
            'codigo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el codigo'}),
            'serial_num': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el numero serial'}),
            'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la marca'}),
            'estado': forms.Select(choices=Inventario.ESTADOS_TYPES, attrs={'class': 'form-control'}),
            'dateAdquired': forms.DateInput(attrs={'type': 'date'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor'}),
            'entregadoA': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese a quien se le entrego'}),
            'redProject': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el area o el proyecto pertinente'}),
            'dateTaken': forms.DateInput(attrs={'type': 'date'}),
            'dateGivenBack': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'name': 'Nombre',
            'cantidad': 'Cantidad',
            'descripcion': 'Descripción',
            'caracteristicas': 'Caracteristicas',
            'codigo': 'Codigo',
            'serial_num': 'Numero Serial',
            'marca': 'Marca',
            'estado': 'Estado',
            'dateAdquired': 'Fecha de Aquisición',
            'valor': 'Valor',
            'entregadoA': 'Entregado A',
            'redProject': 'Red o Projecto',
            'dateTaken': 'Fecha Inicial de Prestamo',
            'dateGivenBack': 'Fecha de Devolución'
        }

    def clean(self):
            cleaned_data = super().clean()
            dateTaken = cleaned_data.get("dateTaken")
            dateGivenBack = cleaned_data.get("dateGivenBack")

            if dateTaken and dateGivenBack and dateTaken > dateGivenBack:
                raise forms.ValidationError("La fecha inicial no puede ser mayor que la fecha de terminación")

            return cleaned_data

class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Observacion
        fields = ['observacion']
        widgets = {
            'observacion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingrese su observación', 'rows': 2, 'cols': 40})
        }
        labels = {
            'observacion': 'Observaciones'
        }

class SedeForm(forms.ModelForm):

    contrato = forms.ModelChoiceField(
        queryset=Task.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Contrato',
    )

    class Meta:
        model = Sede
        fields = ['nombre', 'departamento', 'municipio', 'address', 'latitud', 'longitud', 'lat1', 'lat2', 'lat3', 'lon1', 'lon2', 'lon3', 'descripcion', 'contrato']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la sede'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el departamento donde se encuentra la sede'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el municipio donde se encuentra la sede'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de la sede'}),
            'latitud': forms.Select(choices=Sede.LATITUD, attrs={'class': 'form-control'}),
            'longitud': forms.Select(choices=Sede.LONGITUD, attrs={'class': 'form-control'}),
            'lat1': forms.TextInput(attrs={'class': 'form-control'}),
            'lat2': forms.TextInput(attrs={'class': 'form-control'}),
            'lat3': forms.TextInput(attrs={'class': 'form-control'}),
            'lon1': forms.TextInput(attrs={'class': 'form-control'}),
            'lon2': forms.TextInput(attrs={'class': 'form-control'}),
            'lon3': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingrese la descripción de la sede', 'rows': 2, 'cols': 40}),
        }
        labels = {
            'nombre': 'Nombre Sede',
            'departamento': 'Departamento',
            'municipio': 'Municipio',
            'address': 'Dirección',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'lat1': 'Grados ° Latitud*',
            'lat2': 'Minutos ° Latitud*',
            'lat3': 'Segundos ° Latitud*',
            'lon1': 'Grados ° Longitud*',
            'lon2': 'Minutos ° Longitud*',
            'lon3': 'Segundos ° Longitud*',
            'descripcion': 'Descripción'
        }

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['file']
        widgets = {
        'file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'file': 'Imagen'
        }

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['date', 'hora', 'campo_1_1', 'observacion_1_1', 'campo_1_2', 'observacion_1_2', 'campo_1_3', 'observacion_1_3', 'campo_1_4', 'observacion_1_4', 'campo_1_5', 'observacion_1_5', 'campo_1_6', 'observacion_1_6', 'campo_1_7', 'observacion_1_7', 'campo_2_1', 'observacion_2_1', 'campo_2_2', 'observacion_2_2', 'campo_2_3', 'observacion_2_3', 'campo_2_4', 'observacion_2_4', 'campo_2_5', 'observacion_2_5', 'campo_2_6', 'observacion_2_6', 'campo_2_7', 'observacion_2_7', 'campo_2_8', 'observacion_2_8', 'campo_2_9', 'observacion_2_9', 'campo_3_1', 'observacion_3_1', 'campo_3_2', 'observacion_3_2', 'campo_3_3', 'observacion_3_3', 'campo_3_4', 'observacion_3_4', 'campo_3_5', 'observacion_3_5', 'campo_3_6', 'observacion_3_6', 'campo_3_7', 'observacion_3_7', 'campo_3_8', 'observacion_3_8', 'campo_4_1', 'observacion_4_1', 'campo_4_2', 'observacion_4_2', 'campo_4_3', 'observacion_4_3', 'campo_4_4', 'observacion_4_4', 'campo_4_5', 'observacion_4_5', 'campo_4_6', 'observacion_4_6', 'campo_4_7', 'observacion_4_7', 'campo_4_8', 'observacion_4_8', 'campo_4_9', 'observacion_4_9', 'campo_4_10', 'observacion_4_10', 'campo_4_11', 'observacion_4_11', 'campo_5_1', 'observacion_5_1', 'campo_6_1', 'observacion_6_1', 'campo_6_2', 'observacion_6_2', 'campo_6_3', 'observacion_6_3', 'campo_6_4', 'observacion_6_4', 'campo_7_1', 'observacion_7_1', 'campo_7_2', 'observacion_7_2', 'campo_7_3', 'observacion_7_3', 'campo_7_4', 'observacion_7_4', 'campo_8_1', 'observacion_8_1', 'campo_8_2', 'observacion_8_2', 'campo_8_3', 'observacion_8_3', 'campo_8_4', 'observacion_8_4', 'campo_8_5', 'observacion_8_5', 'campo_9_1', 'observacion_9_1', 'campo_9_2', 'observacion_9_2', 'campo_10_1', 'observacion_10_1', 'campo_10_2', 'observacion_10_2', 'campo_10_3', 'observacion_10_3', 'campo_10_4', 'observacion_10_4', 'campo_10_5', 'observacion_10_5', 'campo_11_1', 'observacion_11_1', 'campo_11_2', 'observacion_11_2', 'campo_11_3', 'observacion_11_3', 'campo_11_4', 'observacion_11_4', 'campo_11_5', 'observacion_11_5', 'campo_11_6', 'observacion_11_6', 'campo_11_7', 'observacion_11_7', 'campo_11_8', 'observacion_11_8', 'campo_11_9', 'observacion_11_9', 'campo_11_10', 'observacion_11_10', 'observacionGeneral']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}), 
            'campo_1_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 'observacion_1_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_6': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_6': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_1_7': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_1_7': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_6': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_6': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_7': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_7': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_8': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_8': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_2_9': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_2_9': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),
            'observacion_3_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),
            'observacion_3_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_6': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_6': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_7': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_7': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_3_8': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_3_8': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_4_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),
            'observacion_4_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_4_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_4_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_4_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_6': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_4_6': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_7': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_4_7': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}),
            'campo_4_8': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_4_8': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_9': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_4_9': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_10': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_4_10': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_4_11': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_4_11': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_5_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),
            'observacion_5_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_6_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_6_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}),
            'campo_6_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_6_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_6_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_6_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_6_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_6_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_7_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_7_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_7_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_7_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_7_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_7_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_7_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_7_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_8_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_8_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_8_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_8_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_8_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_8_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_8_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_8_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_8_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_8_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_9_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_9_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_9_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_9_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_10_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_10_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_10_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_10_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_10_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_10_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_10_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_10_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_10_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_10_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_1': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_1': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_2': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_3': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_4': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),
            'observacion_11_4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_5': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_5': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_6': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_11_6': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_7': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_11_7': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_8': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_8': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}),
            'campo_11_9': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}), 
            'observacion_11_9': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'campo_11_10': forms.Select(choices=Visita.OPCIONES, attrs={'class': 'form-control'}),  
            'observacion_11_10': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observación', 'rows': 2, 'cols': 40}), 
            'observacionGeneral': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese en caso de tener alguna observación general', 'rows': 5, 'cols': 40})
        }

    def clean(self):
        cleaned_data = super().clean()

        max_fields = {
        1: 7,   
        2: 9,  
        3: 8,
        4: 11,
        5: 1,
        6: 4, 
        7: 4,
        8: 5,
        9: 2,
        10: 5,
        11: 10
        }
        
        for section, max_field_count in max_fields.items():
            for field in range(1, max_field_count + 1):
                campo_key = f'campo_{section}_{field}'
                observacion_key = f'observacion_{section}_{field}'

                campo_value = cleaned_data.get(campo_key)
                observacion_value = cleaned_data.get(observacion_key)

                if campo_value == 'NO' and not observacion_value:
                    raise forms.ValidationError(f"El campo observación {section}.{field} no puede quedar vacío si el campo {section}.{field} es igual a 'NO'.")

        return cleaned_data