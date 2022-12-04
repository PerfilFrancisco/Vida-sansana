from django.shortcuts import render
from .models import Taller,Usuario,Sede,Dia,DiaTaller
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

## taller
def crearTv2(request): 
    
    if request.method == "POST":
        Nombre = request.POST.get('nombre')
        profesor = request.POST.get('profesor') 
        descripcion = request.POST.get('descripcion')
        cupom = request.POST.get('cupoM')
        cupoa = request.POST.get('cupoA')
        ubicacion = request.POST.get('ubicacion')
        estado = request.POST.get('estado')
        Hinicio = request.POST.get('hinicio')
        Hfin = request.POST.get('hfin')
        sede = request.POST.get('sede')
        sedeF = Sede.objects.get(sede_id=sede)

        lunes = request.POST.get('lunes')
        martes = request.POST.get('martes')
        miercoles = request.POST.get('miercoles')
        jueves = request.POST.get('jueves')
        viernes = request.POST.get('viernes')
        print(martes)
        Taller.objects.create(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=cupoa,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)        
        id =Taller.objects.get(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=cupoa,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)
        tallerID = id.tall_id
        print(tallerID)
        if lunes != None:
            DiaTaller.objects.create(dia_id=1,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)
        if martes != None:
            martesF = Dia.objects.get(dia_id=martes)
            DiaTaller.objects.create(dia_id=2,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)        
        if miercoles != None:
            miercolesF = Dia.objects.get(dia_id=miercoles)
            DiaTaller.objects.create(dia_id=3,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)
        if jueves != None:
            juevesF = Dia.objects.get(dia_id=jueves)
            DiaTaller.objects.create(dia_id=4,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)     
        if viernes != None:
            viernesF = Dia.objects.get(dia_id=viernes)
            DiaTaller.objects.create(dia_id=5,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)                   

        
        return render(request,'crearT.html')
    elif request.method == "GET":
        return render(request,'crearT.html')

# def crearTv2(request):
#     return render(request,'crearT.html')

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
        try:
            usuario = Usuario.objects.get(usu_correo=request.POST["correo"],usu_contrasena=request.POST["contra"])

        except ObjectDoesNotExist:
            return render(request,'login-fail.html')
        return render(request,'inicio.html',{'usuario':usuario})
    return render(request,'inicio.html')
def blg(request):
    return render(request,'login-fail.html')
def loguear(request):
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
    return render(request,'inicioPymes.html')
def autores(request):
    return render(request, 'autores.html')