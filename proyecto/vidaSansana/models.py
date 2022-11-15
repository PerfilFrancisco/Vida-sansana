from django.db import models

# Create your models here.
class taller(models.Model):
    tall_id = models.AutoField(primary_key=True)
    tall_nombre = models.CharField(max_length=45)
    tall_nombre = models.CharField(max_length=45)
    tall_profesor = models.CharField(max_length=45)
    tall_descripcion = models.CharField(max_length=45)
    tall_cupo_act = models.IntegerField
    tall_cupo_max = models.IntegerField
    
