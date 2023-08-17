from django.shortcuts import render
from django.http import HttpResponse

from .forms import *

from .models import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def clientes(request):
    contexto = {'clientes': Contacto.objects.all(), 'titulo': 'Reporte Clientes' }
    return render(request, "aplicacion/clientes.html", contexto)

def empresa(request):
    contexto = {'empresas': Empresa.objects.all(), 'titulo': 'Reporte de Empresas' }
    return render(request, "aplicacion/empresa.html", contexto)

def garantia(request):
    contexto = {'garantias': Garantia.objects.all(), 'titulo': 'Reporte de Garantías' }
    return render(request, "aplicacion/garantia.html", contexto)

def ingreso_exitoso(request):
    return render(request, "aplicacion/ingreso_exitoso.html")

def empresaform(request):
    if request.method == "POST":
        miForm = empresaForm(request.POST)
        if miForm.is_valid():
            empresa_nombre = miForm.cleaned_data.get('nombre')
            empresa_nit = miForm.cleaned_data.get('nit')
            empresa = Empresa(nombre=empresa_nombre,nit=empresa_nit)
            empresa.save()
            return render(request, "aplicacion/ingreso_exitoso.html")
    else:

        miForm = empresaForm()
    
    return render(request, "aplicacion/empresaform.html", {"form": miForm })


def buscarEmpresa(request):
    return render(request, "aplicacion/buscarEmpresa.html")

def buscarEmpresa2(request):
    
    if request.GET['buscar']:
        patron = request.GET['buscar']        
        empresas = Empresa.objects.filter(nombre__icontains = patron)        
        contexto = {"empresas": empresas, 'titulo': f'Empresas que tiene como patron "{patron}"'}
        return render(request, "aplicacion/empresa.html", contexto)
        
    return HttpResponse("La empresa buscada no se encuenta registrada, intente nuevamente.")
             
             
    
        


