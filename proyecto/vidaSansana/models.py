from django.db import models

# Create your models here.
class Carrera(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=50)

class Dia(models.Model):
    dia_id = models.AutoField(primary_key=True)
    dia_nombre = models.CharField(max_length=20)

class Dia_taller(models.Model):
    dia_id = models.ForeignKey(Dia,on_delete=models.CASCADE)
    tall_id = models.ForeignKey(Taller,on_delete=models.CASCADE)
    dt_hora_incio = models.CharField(max_length=6)
    dt_hora_fin = models.CharField(max_length=6)

class Sede(models.Model):
    sede_id = models.AutoField(primary_key=True)
    sede_nombre = models.CharField(max_length=50)

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

    

