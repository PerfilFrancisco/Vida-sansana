from django.shortcuts import render
from .models import Taller,Usuario

# Create your views here.

## taller
def crearTaller(request): 
    if request.method == "POST":
        Nombre = request.POST.get('nombre')
        profesor = request.POST.get('profesor') 
        descripcion = request.POST.get('descripcion')
        cupo = request.POST.get('cupo')
        ubicacion = request.POST.get('ubicacion')
        estado = request.POST.get('estado')
        Taller.objects.create(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupo)
    elif request.method == "GET":
        return render(request,'inscribir_taller.html')

def crearTv2(request):
    return render(request,'crearT.html')

def inscribir_taller(request):
    return render(request,'crear_talller.html') 

def listaTalleres(request):
    return render(request,'inicioTaller.html')

## sesion
def inicio(request):
    return render(request,'inicio.html')
def carrusel(request):
    
    # if request.method == "POST" and Usuario.objects.filter(usu_correo=correo) and Usuario.objects.filter(usu_contrasena=contra):
    if request.method == "POST":
        usuario = Usuario.objects.get(usu_correo=request.POST["correo"],usu_contrasena=request.POST["contra"])
        print(usuario.tipo_usu)
        return render(request,'carrusel.html',{'usuario':usuario})
    else:
        return render(request,'carrusel.html')
def blg(request):
    return render(request,'login-fail.html')
def loguear(request):
    if request.method == "POST":
        try:
            usuario = Usuario.objects.get(usu_correo=request.POST["correo"],usu_contrasena=request.POST["contra"])
        except ObjectDoesNotExist:
            return render(request,'login-fail.html')
        return render(request,'carrusel.html',{'usuario':usuario})
    return render(request,'login.html')
def registro(request):
    return render(request,'registrarse.html')
def perfil(request):
    return render(request,'perfil.html')

## pymes
def crearPublicacion(request):
    return render(request,'crear_publicacion.html')
def puntuar(request):
    return render(request,'puntuar.html')
def previa(request):
    return render(request,'vista_previa.html')
def lpymes(request):
    return render(request,'listaPymes.html')