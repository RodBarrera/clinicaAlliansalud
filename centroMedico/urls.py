"""centroMedico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from clinicApp.views import agregarSecretaria, startSecretaria, editarSecretaria, eliminarSecretaria, startMedico, \
    agregarMedico, editarMedico, startPaciente, agregarPaciente, editarPaciente, startHoja, agregarHoja, editarHoja, \
    eliminarMedico, eliminarPaciente, eliminarHoja, index, vistaMedico, selVista, vistaSecretaria, permisos, \
    noPermitido, startPacienteMed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secretaria/', startSecretaria, name="secretaria"),
    path('agregar/', agregarSecretaria),
    path('editar/<int:id>', editarSecretaria),
    path('eliminar/<int:id>', eliminarSecretaria),
    path('medico/', startMedico, name="medico"),
    path('agregarmedico/', agregarMedico),
    path('editarmedico/<int:id>', editarMedico),
    path('eliminarmedico/<int:id>', eliminarMedico),
    path('paciente/', startPaciente, name="paciente"),
    path('pacientemed/', startPacienteMed, name="pacientemed"),
    path('agregarpaciente/', agregarPaciente),
    path('editarpaciente/<int:id>', editarPaciente),
    path('eliminarpaciente/<int:id>', eliminarPaciente),
    path('hojaatencion/', startHoja, name="hoja"),
    path('agregarhoja/', agregarHoja),
    path('editarhoja/<int:id>', editarHoja),
    path('eliminarhoja/<int:id>', eliminarHoja),
    path('', index),
    path('vistamedico/', vistaMedico),
    path('vistasecretaria/', vistaSecretaria),
    path('seleccionvista', selVista),
    path('permisos/', permisos),
    path('no-permitido/', noPermitido)
]
