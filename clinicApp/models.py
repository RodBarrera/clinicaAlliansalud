from django.db import models

# Create your models here.

class Secretaria(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)




class Especialidades(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.name}'


class Medico(models.Model):

    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)
    category = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)


class Paciente(models.Model):

    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    dateB = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=25)
    Comuna = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    emergencyContact = models.CharField(max_length=25)
    emergencyPhone = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    health = models.CharField(max_length=25)


class HojaAtencion(models.Model):

    profesionalAtendio = models.CharField(max_length=25)
    anamnesisAnterior =  models.CharField(max_length=250)
    medicamentosRecetados = models.CharField(max_length=250)
    examenesSolicitados = models.CharField(max_length=250)
    alergias = models.CharField(max_length=125)
    historialEnfermedades = models.CharField(max_length=500)
    medicamentosQueToma = models.CharField(max_length=250)
    diagnosticoObtenido= models.CharField(max_length=500)
    observaciones = models.CharField(max_length=250)






