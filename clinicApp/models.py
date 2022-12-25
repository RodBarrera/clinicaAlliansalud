from django.db import models
from django import forms
# Create your models here.

class Secretaria(models.Model):
    Rut = models.CharField(max_length=12)
    Nombres = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=25, verbose_name='Apellido Paterno')
    Apellido_Materno = models.CharField(max_length=25)

class Especialidades(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.name}'


class Medico(models.Model):

    Rut = models.CharField(max_length=12)
    Nombres = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=25)
    Apellido_Materno = models.CharField(max_length=25)
    Categoria = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)



class Paciente(models.Model):

    Rut = models.CharField(max_length=12)
    Nombres = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=25)
    Apellido_Materno = models.CharField(max_length=25)
    Fecha_Nacimiento = models.DateTimeField(blank=True, null=True)
    Genero = models.CharField(max_length=25)
    Direccion = models.CharField(max_length=25)
    Comuna = models.CharField(max_length=25)
    Nacionalidad = models.CharField(max_length=25)
    Telefono = models.CharField(max_length=25)
    Contacto_de_Emergencia = models.CharField(max_length=25)
    Telefono_de_Emergencia = models.CharField(max_length=25)
    Sistema_de_Salud = models.CharField(max_length=25)


class HojaAtencion(models.Model):

    Rut_Paciente = models.CharField(max_length=25)
    Profesional_que_Atendio = models.CharField(max_length=25)
    Fecha_Atencion = models.DateTimeField(blank=True, null=True)
    Alergias = models.CharField(max_length=125)
    Historial_de_Enfermedades = models.CharField(max_length=500)
    Medicamentos_que_toma = models.CharField(max_length=250)
    Anamnesis = models.TextField(max_length=250)
    Diagnostico = models.TextField(max_length=500)
    Medicamentos_Recetados = models.CharField(max_length=250)
    Examenes_Solicitados = models.CharField(max_length=250)
    Observaciones = models.TextField(max_length=250)






