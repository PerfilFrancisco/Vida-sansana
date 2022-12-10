from django.shortcuts import render,redirect
from .models import Taller,Usuario,Sede,Dia,DiaTaller,AuthUser,TipoUsuario,Hito,HitoSede
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,authenticate,logout
from django.views.generic import View
from django.contrib import auth


# Create your views here.


########################## seccion inicio #######################
def inicio(request):
    #aglkjklug
    # correo = request.session['usuarioCorreo']
    hitos = Hito.objects.all()    
    hitosede = HitoSede.objects.all()
    #print(hitosede[0].hito.hito_id)
    
    if request.method == "POST":   
        try:
            usuario = Usuario.objects.get(usu_correo=request.POST["correo"],usu_contrasena=request.POST["contraseña"])

            request.session['usuarioCorreo'] = usuario.usu_correo
            
        except ObjectDoesNotExist:
            return render(request,'login-fail.html')
        
        return render(request,'inicio.html',{'usuario':usuario,'hitos':hitos,'sede':sede})

    else:
        if 'usuarioCorreo' not in request.session:
            return render(request,'inicio.html',{'hitos':hitos})
        else:
            correo = request.session['usuarioCorreo']
            usuario = Usuario.objects.get(usu_correo=correo)
            
            return render(request,'inicio.html',{'usuario':usuario,'hitos':hitos})

def blg(request):
    return render(request,'login-fail.html')

def loguear(request):
    return render(request,'login.html')

def registro(request):
    if 'usuarioCorreo' not in request.session:
        return render(request,'registrarse.html')
    else:
        correo = request.session['usuarioCorreo']
        usuario = Usuario.objects.get(usu_correo=correo)
        
        return render(request,'registrarse.html',{'usuario':usuario})
    
    return render(request,'registrarse.html')

def perfil(request):
    if request.method == "POST":
        del request.session['usuarioCorreo']
        
        return render(request, 'inicio.html')
    return render(request,'perfil.html')

def autores(request):
    if 'usuarioCorreo' not  in request.session:
        return render(request,'autores.html')
    else:
        correo = request.session['usuarioCorreo']
        usuario = Usuario.objects.get(usu_correo=correo)
        
        return render(request,'autores.html',{'usuario':usuario})
    
    

########################## seccion de talleres ##########################

def listaTalleres(request):
    taller = Taller.objects.filter()
    
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        usuario = Usuario.objects.get(usu_correo=correo)
        if correo == usuario.usu_correo:
            tipo = TipoUsuario.objects.get(tipo_usu_id=2)
            return render(request,'inicioTaller.html',{'usuario':usuario,'talleres':taller})
    else:
        
        return render(request,'inicioTaller.html',{'talleres':taller})


def crearTv2(request): 
    
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        usuario = Usuario.objects.get(usu_correo=correo)
        tusuario = TipoUsuario.objects.get(tipo_usu_id=2)
        if request.method == "GET" and usuario.tipo_usu == tusuario:
            return render(request,'crearT.html',{'usuario':usuario})

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

        Taller.objects.create(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=cupoa,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)        
        id =Taller.objects.get(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=cupoa,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)
        tallerID = id.tall_id

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

        
        return render(request,'crearT.html',{'usuario':usuario})
    else:
        return render(request,'inicioTaller.html')



def inscribir_taller(request):
    
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        Uscorreo = Usuario.objects.get(usu_correo=correo)
        if correo == Uscorreo.usu_correo:
            
            return render(request,'inscribir_taller.html',{'usuario':Uscorreo})
    return render(request,'inscribir_taller.html') 

def verTaller(request):
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        Uscorreo = Usuario.objects.get(usu_correo=correo)
        if correo == Uscorreo.usu_correo:
            
            return render(request,'ver_taller.html',{'usuario':Uscorreo})
    return render(request,'ver_taller.html')

############################### seccion Pymes ######################
 
def crearPublicacion(request):
    return render(request,'crear_publicacion.html')
def puntuar(request):
    return render(request,'puntuar.html')
def lpymes(request):
    
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
    
        usuario = Usuario.objects.get(usu_correo=correo)
        if correo == usuario.usu_correo:
            
            return render(request,'inicioPymes.html',{'usuario':usuario})
    else:
        return render(request,'inicioPymes.html')



####################### externo #############################
def previa(request):
    return render(request,'vista_previa.html')
