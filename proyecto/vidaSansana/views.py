from django.shortcuts import render

# Create your views here.
def crearTaller(request):
    return render(request,'crear_taller.html')
def inicio(request):
    return render(request,'inicio.html')