from django.shortcuts import render
from .models import Taller
# Create your views here.
def crearTaller(request):
    if request.method == "POST":
        Nombre = request.POST.get('nombre')
        profesor = request.POST.get('profesor') 
        descripcion = request.POST.get('descripcion')
        cupo = request.POST.get('cupo')
        Taller.objects.create(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupo)
    return render(request,'crear_taller.html') 

def inicio(request):
    return render(request,'inicio.html')
def crearPublicacion(request):
    return render(request,'crear_publicacion.html')
def loguear(request):
    return render(request,'login.html')
def carrusel(request):
    return render(request,'carrusel.html')
def inscribir(request):
    return render(request,'inscribir_taller.html')
def puntuar(request):
    return render(request,'puntuar.html')
def previa(request):
    return render(request,'vista_previa.html')