from django.db import models

# Create your models here.
class carrera(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=50)

class dia(models.Model):
    dia_id = models.AutoField(primary_key=True)
    dia_nombre = models.CharField(max_length=20)

class 

    

