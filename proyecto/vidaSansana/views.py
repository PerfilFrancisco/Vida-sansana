from django.shortcuts import render,redirect
from .models import Taller,Usuario,Sede,Dia,DiaTaller,AuthUser,TipoUsuario,Hito,HitoSede,Carrera,DiaTaller,TallUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,authenticate,logout
from django.views.generic import View
from django.contrib import auth
from django.contrib import messages


# Create your views here.


########################## seccion inicio #######################
def inicio(request):
    #aglkjklug
    # correo = request.session['usuarioCorreo']
    hitos = Hito.objects.all()    
    hitosede = HitoSede.objects.all()
    #print(hitosede[0].hito.hito_id)
    
    if request.method == "POST":   
        correo = request.POST.get('correo')
        contra = request.POST.get('contraseña')
        nombre = request.POST.get('nombre')

        if Usuario.objects.filter(usu_correo=correo,usu_contrasena=contra).exists() and nombre == None:
            usuario = Usuario.objects.get(usu_correo=correo,usu_contrasena=contra)
            request.session['usuarioCorreo'] = usuario.usu_correo            
            return render(request,'inicio.html',{'usuario':usuario,'hitos':hitos})
        elif nombre != None:
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            contraseña = request.POST.get('contra')
            sede = request.POST.get('sede')
            carrera = request.POST.get('carrera')
            rut = request.POST.get('rut')
            sedeF = Sede.objects.get(sede_id=sede)
            tipoF = TipoUsuario.objects.get(tipo_usu_id=3)
            carF = Carrera.objects.get(car_id=carrera)            
            usuario = Usuario.objects.create(usu_rut=rut,usu_correo=correo,usu_nombre=nombre,usu_contrasena=contraseña,sede=sedeF,tipo_usu=tipoF,car=carF)
            request.session['usuarioCorreo'] = usuario.usu_correo 
            return render(request,'inicio.html',{'usuario':usuario,'hitos':hitos})
        else:
            messages.add_message(request=request , level=messages.ERROR , message="Inicio de sesion incorrecto")
            return render(request , 'login.html')
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

def resultados(request):
    hitos = Hito.objects.filter(hito_fecha_inicio__gt=request.POST.get('fecha'))
    # hitos = Hito.objects.filter(hito_fecha_inicio__range=["2022-10-21", "2022-10-30"])
    
    return render(request,'resultados.html',{'hitos':hitos})

########################## seccion de talleres ##########################



def crearTv2(request): 
    
    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        usuario = Usuario.objects.get(usu_correo=correo)
        tusuario = TipoUsuario.objects.get(tipo_usu_id=2)
        if request.method == "GET" and usuario.tipo_usu == tusuario:
            return render(request,'crearT.html',{'usuario':usuario})

    if request.method == "POST":
        #datos simples
        Nombre = request.POST.get('nombre')
        profesor = request.POST.get('profesor') 
        descripcion = request.POST.get('descripcion')
        cupom = request.POST.get('cupoM')        
        ubicacion = request.POST.get('ubicacion')
        estado = request.POST.get('estado')
        sede = request.POST.get('sede')
        sedeF = Sede.objects.get(sede_id=sede)

        #datos horario
        lunes = request.POST.get('lunes')
        martes = request.POST.get('martes')
        miercoles = request.POST.get('miercoles')
        jueves = request.POST.get('jueves')
        viernes = request.POST.get('viernes')

        Taller.objects.create(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=0,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)        
        id =Taller.objects.get(tall_nombre=Nombre,tall_profesor=profesor,tall_descripcion=descripcion,tall_cupo_max=cupom,tall_cupo_act=0,sede=sedeF,tall_estado=estado,tall_ubicacion=ubicacion)
        tallerID = id.tall_id
        print(lunes)
        if lunes != None:
            Hinicio = request.POST.get('Hinicio1')
            Hfin = request.POST.get('Hfin1')
            DiaTaller.objects.create(dia_id=1,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)
        if martes != None:
            Hinicio = request.POST.get('Hinicio2')
            Hfin = request.POST.get('Hfin2')     
            martesF = Dia.objects.get(dia_id=martes)
            DiaTaller.objects.create(dia_id=2,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)        
        if miercoles != None:
            Hinicio = request.POST.get('Hinicio3')
            Hfin = request.POST.get('Hfin3')         
            miercolesF = Dia.objects.get(dia_id=miercoles)
            DiaTaller.objects.create(dia_id=3,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)
        if jueves != None:
            Hinicio = request.POST.get('Hinicio4')
            Hfin = request.POST.get('Hfin4')        
            juevesF = Dia.objects.get(dia_id=jueves)
            DiaTaller.objects.create(dia_id=4,tall=id,dt_hora_incio=Hinicio,dt_hora_fin=Hfin)     
        if viernes != None:
            Hinicio = request.POST.get('Hinicio5')
            Hfin = request.POST.get('Hfin5')        
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

def verTaller(request,id):
    #tomo el taller por el id que paso por la url
    taller = Taller.objects.get(tall_id=id)
    horario = DiaTaller.objects.filter(tall=taller.tall_id)
    

    if "usuarioCorreo" in request.session:
        correo = request.session['usuarioCorreo']
        Uscorreo = Usuario.objects.get(usu_correo=correo)
        if correo == Uscorreo.usu_correo:
            if request.method == "POST":
                #print(hitosede[0].hito.hito_id)
                # Id = Usuario.objects.get(usu_rut=Uscorreo.usu_rut)
                # ID = Id.usu_rut
                # ta = Usuario.objects.get(tall=taller.tall_id)
                # TA = ta.tall
                tu = TallUsuario.objects.filter(usu_rut=None,tall=None)
                tu.usu_rut = Uscorreo.usu_rut
                tu.tall = taller.tall_id
                tu.save()
                
                #TallUsuario.objects.create(usu_rut=Uscorreo.usu_rut,tall=taller.tall_id)
                return render(request,'ver_taller.html',{'usuario':Uscorreo,'taller':taller,'horarios':horario} )
            return render(request,'ver_taller.html',{'usuario':Uscorreo,'taller':taller,'horarios':horario} )
    else:
        return render(request,'inicioTaller.html',{'taller':taller})
    

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
