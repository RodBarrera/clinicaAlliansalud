from django.contrib import admin

from clinicApp.models import Secretaria, Especialidades, Medico, Paciente, HojaAtencion


class SecretariaAdmin(admin.ModelAdmin):
    list_display = ['id','Rut','Nombres','Apellido_Paterno', 'Apellido_Materno']

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class MedicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Rut', 'Nombres', 'Apellido_Paterno', 'Apellido_Materno', 'Categoria']

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'Rut', 'Nombres', 'Apellido_Paterno', 'Apellido_Materno', 'Genero', 'Fecha_Nacimiento', 'Direccion', 'Comuna', 'Telefono', 'Contacto_de_Emergencia', 'Telefono_de_Emergencia', 'Nacionalidad', 'Sistema_de_Salud']

class HojaAdmin(admin.ModelAdmin):
    list_display = ['id', 'Profesional_que_Atendio', 'Anamnesis', 'Medicamentos_Recetados', 'Examenes_Solicitados', 'Alergias', 'Historial_de_Enfermedades', 'Medicamentos_que_toma','Diagnostico', 'Observaciones']

# Register your models here.

admin.site.register(Secretaria, SecretariaAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(HojaAtencion, HojaAdmin)

