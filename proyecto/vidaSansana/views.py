from django.shortcuts import render
from django import forms
from .forms import crearTa
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
