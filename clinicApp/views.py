from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

from clinicApp.models import Secretaria, Medico, Paciente, HojaAtencion


# Create your views here.

def startSecretaria(request):

    secretarias = Secretaria.objects.all()
    data = {
        'secretarias': secretarias

        }
    return render(request, 'secretaria.html', data)

SecretariaForm = modelform_factory(Secretaria, exclude=[])
MedicoForm = modelform_factory(Medico, exclude=[])
PacienteForm = modelform_factory(Paciente, exclude=[])
HojaForm = modelform_factory(HojaAtencion, exclude=[])

def agregarSecretaria(request):
    if request.method == 'POST':
        formularioSecretaria = SecretariaForm(request.POST)
        if formularioSecretaria.is_valid():
            formularioSecretaria.save()
            return redirect('secretaria')


    else:
        formularioSecretaria = SecretariaForm()

    data = {'formularioSecretaria': formularioSecretaria}
    return render(request, "agregar-secretaria.html",data)

def editarSecretaria(request,id):
    secretaria = get_object_or_404(Secretaria, pk= id)
    if request.method == 'POST':
        formularioSecretaria = SecretariaForm(request.POST, instance=secretaria)
        if formularioSecretaria.is_valid():
            formularioSecretaria.save()
            return redirect('secretaria')


    else:
        formularioSecretaria = SecretariaForm(instance=secretaria)

    data = {'formularioSecretaria': formularioSecretaria}
    return render(request, "editar-secretaria.html",data)


def eliminarSecretaria(request, id):
    secretaria = get_object_or_404(Secretaria, pk= id)

    if secretaria:
        secretaria.delete()

    return redirect('secretaria')

def startMedico(request):

    medicos = Medico.objects.all()
    data = {
        'medicos': medicos

        }
    return render(request, 'medico.html', data)


def agregarMedico(request):
    if request.method == 'POST':
        formularioMedico = MedicoForm(request.POST)
        if formularioMedico.is_valid():
            formularioMedico.save()
            return redirect('medico')


    else:
        formularioMedico = MedicoForm()

    data = {'formularioMedico': formularioMedico}
    return render(request, "agregar-medico.html",data)


def editarMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    if request.method == 'POST':
        formularioMedico = MedicoForm(request.POST, instance=medico)
        if formularioMedico.is_valid():
            formularioMedico.save()
            return redirect('medico')


    else:
        formularioMedico = MedicoForm(instance=medico)

    data = {'formularioMedico': formularioMedico}
    return render(request, "editar-medico.html",data)


def eliminarMedico(request, id):
    medico = get_object_or_404(Medico, pk= id)

    if medico:
        medico.delete()

    return redirect('medico')


def startPaciente(request):

    pacientes = Paciente.objects.all()
    data = {
        'pacientes': pacientes

        }
    return render(request, 'paciente.html', data)

def agregarPaciente(request):
    if request.method == 'POST':
        formularioPaciente = PacienteForm(request.POST)
        if formularioPaciente.is_valid():
            formularioPaciente.save()
            return redirect('paciente')


    else:
        formularioPaciente = PacienteForm()

    data = {'formularioPaciente': formularioPaciente}
    return render(request, "agregar-paciente.html",data)

def editarPaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        formularioPaciente = PacienteForm(request.POST, instance=paciente)
        if formularioPaciente.is_valid():
            formularioPaciente.save()
            return redirect('paciente')


    else:
        formularioPaciente = PacienteForm(instance=paciente)

    data = {'formularioPaciente': formularioPaciente}
    return render(request, "agregar-paciente.html",data)


def eliminarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk= id)

    if paciente:
        paciente.delete()

    return redirect('paciente')


def startHoja(request):

    hojaAtencion = HojaAtencion.objects.all()
    data = {
        'hojaAtencion': hojaAtencion

        }
    return render(request, 'hoja-atencion.html', data)

def agregarHoja(request):
    if request.method == 'POST':
        formularioHoja = HojaForm(request.POST)
        if formularioHoja.is_valid():
            formularioHoja.save()
            return redirect('hoja')


    else:
        formularioHoja = HojaForm()

    data = {'formularioHoja': formularioHoja}
    return render(request, "agregar-hoja.html",data)


def editarHoja(request,id):
    hoja = get_object_or_404(HojaAtencion, pk=id)
    if request.method == 'POST':
        formularioHoja = HojaForm(request.POST, instance=hoja)
        if formularioHoja.is_valid():
            formularioHoja.save()
            return redirect('hoja')


    else:
        formularioHoja = HojaForm(instance=hoja)

    data = {'formularioHoja': formularioHoja}
    return render(request, "editar-hoja.html",data)


def eliminarHoja(request, id):
    hoja = get_object_or_404(HojaAtencion, pk= id)

    if hoja:
        hoja.delete()

    return redirect('hoja')


def index(request):
    return render(request, 'index.html')

def vistaMedico(request):
    return render(request, 'vista-medico.html')

def vistaSecretaria(request):
    return render(request, 'vista-secretaria.html')

def selVista(request):
    return render(request, 'seleccion-vista.html')