from django.db import models

# Create your models here.
class Carrera(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=50)

class Dia(models.Model):
    dia_id = models.AutoField(primary_key=True)
    dia_nombre = models.CharField(max_length=20)

class Sede(models.Model):
    sede_id = models.AutoField(primary_key=True)
    sede_nombre = models.CharField(max_length=50)

class Tipo_usu(models.Model):
    tipo_usu_id = models.AutoField(primary_key=True)
    tipo_usu_nombre = models.CharField(max_length=30)

class Usuario(models.Model):
    usu_rut = models.CharField(primary_key=True)
    usu_nombre = models.CharField(max_length=50)
    usu_apellido = models.CharField(max_length=50)
    usu_correo = models.CharField(max_length=50)
    usu_contraseña = models.CharField(max_length=50)
    sede_id = models.ForeignKey(Sede,on_delete=models.CASCADE)
    tipo_usu = models.ForeignKey(Tipo_usu,on_delete=models.CASCADE)

class Hito(models.Model):
    hito_id = models.AutoField(primary_key=True)
    hito_actividad = models
    hito_docencia = models
    hito_reglamentario = models
    hito_fecha_inicio = models
    hito_fecha_fin = models

class Hito_sede(models.Model):
    hito_id = models.ForeignKey(Hito,on_delete=models)
    sede_id = models.ForeignKey(Sede,on_delete=models)

class Publicacion_py(models.Model):
    publ_id = models.AutoField(primary_key=True)
    publ_nombre = models.CharField(max_length=50)
    publ_descripcion = models.CharField(max_length=50)
    publ_ubicacion = models.CharField(max_length=50)
    publ_precio = models.IntegerChoices()
    publ_creacion = models.CharField(max_length=50)
    publ_stock = models.IntegerField()
    publ_visivilidad = models.BinaryField()

class Taller(models.Model):
    tall_id = models.AutoField(primary_key=True)
    tall_nombre = models.CharField(max_length=50)
    tall_profesor = models.CharField(max_length=50)
    tall_descripcion = models.CharField(max_length=50)
    tall_cupo_act = models.CharField(max_length=50)
    tall_cupo_max = models.CharField(max_length=50)
    tall_estado = models.BinaryField()
    tall_ubicacion = models.CharField(max_length=50)
    sede_id = models.ForeignKey(Sede,on_delete=models.CASCADE)

class Usu_taller(models.Model):
    usu_rut = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tall_id = models.ForeignKey(Taller,on_delete=models.CASCADE)

class Dia_taller(models.Model):
    dia_id = models.ForeignKey(Dia,on_delete=models.CASCADE)
    tall_id = models.ForeignKey(Taller,on_delete=models.CASCADE)
    dt_hora_incio = models.CharField(max_length=6)
    dt_hora_fin = models.CharField(max_length=6)

class Usu_publicacion(models.Model):
    usu_rut = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    publ_id = models.ForeignKey(Publicacion_py,on_delete=models.CASCADE)
    


    

