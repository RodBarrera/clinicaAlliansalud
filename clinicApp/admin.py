from django.contrib import admin

from clinicApp.models import Secretaria, Especialidades, Medico, Paciente, HojaAtencion


class SecretariaAdmin(admin.ModelAdmin):
    list_display = ['id','rut','nombres','apellido_p', 'apellido_m']

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class MedicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'rut', 'nombres', 'apellido_p', 'apellido_m', 'category']

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'rut', 'nombres', 'apellido_p', 'apellido_m', 'gender', 'dateB', 'address', 'Comuna', 'phone', 'emergencyContact', 'emergencyPhone', 'country', 'health']

class HojaAdmin(admin.ModelAdmin):
    list_display = ['id', 'profesionalAtendio', 'anamnesisAnterior', 'medicamentosRecetados', 'examenesSolicitados', 'alergias', 'historialEnfermedades', 'medicamentosQueToma','diagnosticoObtenido', 'observaciones']

# Register your models here.

admin.site.register(Secretaria, SecretariaAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(HojaAtencion, HojaAdmin)

