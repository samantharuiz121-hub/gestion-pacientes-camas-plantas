from django.shortcuts import render
from Academica.models import Paciente, Cama, Planta

# Create your views here.

## Pacientes

def listaPacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listado_pacientes.html',
                 {'pacientes': pacientes})

## Plantas

def listaPlantas(request):
    plantas = Planta.objects.all()
    return render(request, 'plantas/listado_plantas.html',
                  {'plantas': plantas})

## Camas

def listaCamas(request):
    camas = Cama.objects.select_related('numero_planta', 'cedula_paciente')
    return render(request, 'camas/listado_camas.html',
                  {'camas': camas})
