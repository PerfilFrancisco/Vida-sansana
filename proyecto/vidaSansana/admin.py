# Register your models here.
from django.contrib import admin
from .models import Carrera,Dia,DiaTaller,Hito,HitoSede,PublicacionPy,Sede,TallUsuario,Taller,TipoUsuario,Usuario,UsuarioPubl,Puntuacion

class CarreraAdmin(admin.ModelAdmin):
      list_display = ['car_id', 'car_nombre']
class DiaAdmin(admin.ModelAdmin):
      list_display = ['dia_id', 'dia_nombre']
class DiaTallerAdmin(admin.ModelAdmin):
      list_display = ['dia', 'tall','dt_hora_incio','dt_hora_fin']
class HitoAdmin(admin.ModelAdmin):
      list_display = ['hito_id']
class HitoSedeAdmin(admin.ModelAdmin):
      list_display = ['hito', 'sede']
class PublicacionPyAdmin(admin.ModelAdmin):
      list_display = ['publ_id', 'publ_nombre','publ_descripcion','publ_ubicacion','publ_precio','publ_creacion','publ_stock','publ_visibilidad']
class SedeAdmin(admin.ModelAdmin):
      list_display = ['sede_id', 'sede_nombre']
class TallUsuarioAdmin(admin.ModelAdmin):
      list_display = ['usu_rut', 'tall']
class TallerAdmin(admin.ModelAdmin):
      list_display = ['tall_id', 'tall_nombre','tall_profesor','tall_descripcion','tall_cupo_act','tall_cupo_max','tall_estado','tall_ubicacion','sede']
class TipoUsuarioAdmin(admin.ModelAdmin):
      list_display = ['tipo_usu_id', 'tu_nombre']
class UsuarioAdmin(admin.ModelAdmin):
      list_display = ['usu_rut', 'usu_nombre','usu_apellido','usu_correo','usu_contrasena','sede','tipo_usu','car']
class UsuarioPublAdmin(admin.ModelAdmin):
      list_display = ['usu_rut', 'publ']
class PuntuacionAdmin(admin.ModelAdmin):
      list_display = ['puntuacion','id_puntuacion','usu_rut','publ_id']
admin.site.register(Puntuacion,PuntuacionAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Dia,DiaAdmin)
admin.site.register(DiaTaller,DiaTallerAdmin)
admin.site.register(Hito,HitoAdmin)
admin.site.register(HitoSede,HitoAdmin)
admin.site.register(PublicacionPy,PublicacionPyAdmin)
admin.site.register(Sede,SedeAdmin)
admin.site.register(TallUsuario,TallUsuarioAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(TipoUsuario,TipoUsuarioAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(UsuarioPubl,UsuarioPublAdmin)
