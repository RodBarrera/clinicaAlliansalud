from django.contrib.auth.decorators import permission_required
from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

import clinicApp.views
from clinicApp.forms import SecretariaForm, MedicoForm, PacienteForm, HojaForm
from clinicApp.models import Secretaria, Medico, Paciente, HojaAtencion

from django.db.models import Q
# Create your views here.

@permission_required('clinicApp.add_secretaria')
def startSecretaria(request):

    secretarias = Secretaria.objects.all()
    data = {
        'secretarias': secretarias

        }
    return render(request, 'secretaria.html', data)

#SecretariaForm = modelform_factory(Secretaria, exclude=[])
#MedicoForm = modelform_factory(Medico, exclude=[])
#PacienteForm = modelform_factory(Paciente, exclude=[])
#HojaForm = modelform_factory(HojaAtencion, exclude=[])

@permission_required('clinicApp.add_secretaria')
def agregarSecretaria(request):
    if request.method == 'POST':
        formularioSecretaria = SecretariaForm(request.POST)
        if formularioSecretaria.is_valid():
            secre = formularioSecretaria.cleaned_data
            secretaria = Secretaria(
                Rut=secre['Rut'],
                Nombres=secre['Nombres'],
                Apellido_Paterno=secre['Apellido_Paterno'],
                Apellido_Materno=secre['Apellido_Materno'],
            )
            #secretaria.save()
            form = ''
            formularioSecretaria.save()
            return redirect('secretaria')


    else:
        formularioSecretaria = SecretariaForm()

    data = {'formularioSecretaria': formularioSecretaria}
    return render(request, "agregar-secretaria.html", data)

@permission_required('clinicApp.add_secretaria')
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

@permission_required('clinicApp.delete_secretaria')
def eliminarSecretaria(request, id):
    secretaria = get_object_or_404(Secretaria, pk= id)

    if secretaria:
        secretaria.delete()

    return redirect('secretaria')
@permission_required('clinicApp.add_medico')
def startMedico(request):
    queryset= request.GET.get("buscar")
    print(queryset)
    medicos = Medico.objects.all()
    if queryset:
        medicos = Medico.objects.filter(
            Q(Rut=queryset) |
            Q(Apellido_Paterno=queryset)
        ).distinct()
    return render(request, 'medico.html', {"medicos": medicos})

@permission_required('clinicApp.add_medico')
def agregarMedico(request):
    if request.method == 'POST':
        formularioMedico = MedicoForm(request.POST)
        if formularioMedico.is_valid():
            medic = formularioMedico.cleaned_data
            medico = Medico(
                Rut=medic['Rut'],
                Nombres=medic['Nombres'],
                Apellido_Paterno=medic['Apellido_Paterno'],
                Apellido_Materno=medic['Apellido_Materno'],
                Categoria=medic['Categoria'],

                #Nombres = models.CharField(max_length=50)
                #Apellido_Paterno = models.CharField(max_length=25)
                #Apellido_Materno = models.CharField(max_length=25)
                #Categoria = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
            )
            #medico.save()
            formularioMedico.save()
            return redirect('medico')


    else:
        formularioMedico = MedicoForm()

    data = {'formularioMedico': formularioMedico}
    return render(request, "agregar-medico.html",data)

@permission_required('clinicApp.add_medico')
def editarMedico(request, id):
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

@permission_required('clinicApp.delete_medico')
def eliminarMedico(request, id):
    medico = get_object_or_404(Medico, pk= id)

    if medico:
        medico.delete()

    return redirect('medico')

def startPaciente(request):
    queryset= request.GET.get("buscar")
    print(queryset)
    pacientes = Paciente.objects.filter()
    if queryset:
        pacientes = Paciente.objects.filter(
            Q(Nombres=queryset) |
            Q(Rut=queryset)
        ).distinct()
    return render(request, 'paciente.html', {"pacientes": pacientes})

def startPacienteMed(request):
    queryset= request.GET.get("buscar")
    print(queryset)
    pacientes = Paciente.objects.filter()
    if queryset:
        pacientes = Paciente.objects.filter(
            Q(Nombres=queryset) |
            Q(Rut=queryset)
        ).distinct()
    return render(request, 'pacientemed.html', {"pacientes": pacientes})

@permission_required('clinicApp.add_paciente')
def agregarPaciente(request):
    if request.method == 'POST':
        formularioPaciente = PacienteForm(request.POST)
        if formularioPaciente.is_valid():
            paci = formularioPaciente.cleaned_data
            paciente = Paciente(
                Rut= paci['Rut'],
                Apellido_Paterno=paci['Apellido_Paterno'],
                Apellido_Materno=paci['Apellido_Materno'],
                Genero=paci['Genero'],
                Fecha_Nacimiento=paci['Fecha_Nacimiento'],
                Direccion=paci['Direccion'],
                Comuna=paci['Comuna'],
                Telefono=paci['Telefono'],
                Contacto_de_Emergencia=paci['Contacto_de_Emergencia'],
                Telefono_de_Emergencia=paci['Telefono_de_Emergencia'],
                Nacionalidad=paci['Nacionalidad'],
                Sistema_de_Salud=paci['Sistema_de_Salud']
            )
            #paciente.save()
            formularioPaciente.save()
            return redirect('paciente')


    else:
        formularioPaciente = PacienteForm()

    data = {'formularioPaciente': formularioPaciente}
    return render(request, "agregar-paciente.html",data)

@permission_required('clinicApp.change_paciente')
def editarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        formularioPaciente = PacienteForm(request.POST, instance=paciente)
        if formularioPaciente.is_valid():
            formularioPaciente.save()
            return redirect('paciente')
    else:
        formularioPaciente = PacienteForm(instance=paciente)

    data = {'formularioPaciente': formularioPaciente}
    return render(request, "editar-paciente.html",data)

@permission_required('clinicApp.delete_paciente')
def eliminarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk= id)

    if paciente:
        paciente.delete()

    return redirect('paciente')

@permission_required('clinicApp.add_hojaatencion')
def startHoja(request):

    hojaAtencion = HojaAtencion.objects.all()
    data = {
        'hojaAtencion': hojaAtencion

        }
    return render(request, 'hoja-atencion.html', data)

@permission_required('clinicApp.add_hojaatencion')
def agregarHoja(request):
    if request.method == 'POST':
        formularioHoja = HojaForm(request.POST)
        if formularioHoja.is_valid():
            hoj = formularioHoja.cleaned_data
            hoja = HojaAtencion(
                Rut_Paciente=hoj['Rut_Paciente'],
                Profesional_que_Atendio= hoj['Profesional_que_Atendio'],
                Fecha_Atencion=hoj['Fecha_Atencion'],
                Anamnesis=hoj['Anamnesis'],
                Medicamentos_Recetados=hoj['Medicamentos_Recetados'],
                Examenes_Solicitados=hoj['Examenes_Solicitados'],
                Alergias=hoj['Alergias'],
                Historial_de_Enfermedades=hoj['Historial_de_Enfermedades'],
                Medicamentos_que_toma=hoj['Medicamentos_que_toma'],
                Diagnostico=hoj['Diagnostico'],
                Observaciones=hoj['Observaciones'],
            )
            #hoja.save()
            formularioHoja.save()
            return redirect('hoja')


    else:
        formularioHoja = HojaForm()

    data = {'formularioHoja': formularioHoja}
    return render(request, "agregar-hoja.html",data)


@permission_required('clinicApp.change_hojaatencion')
def editarHoja(request, id):
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

@permission_required('clinicApp.delete_hojaatencion')
def eliminarHoja(request, id):
    hoja = get_object_or_404(HojaAtencion, pk= id)
    if hoja:
        hoja.delete()

    return redirect('hoja')

def index(request):
    return render(request, 'index.html')

@permission_required('clinicApp.add_hojaatencion')
def vistaMedico(request):
    return render(request, 'vista-medico.html')

@permission_required('clinicApp.add_secretaria')
def vistaSecretaria(request):
    return render(request, 'vista-secretaria.html')

def selVista(request):
    return render(request, 'seleccion-vista.html')

def permisos(request):
    return render(request, 'permisos.html')

def noPermitido(request):
    return render(request, 'no-permitido.html')
