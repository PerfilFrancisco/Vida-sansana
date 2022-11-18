from django import forms
from .models import Carrera,Dia,DiaTaller,Hito,HitoSede,PublicacionPy,Sede,TallUsuario,Taller,TipoUsuario,Usuario,UsuarioPubl

class crearTa(forms.Form):
      nombre = forms.CharField(label="formGroupExampleInput")
      descripcion = forms.CharField(label="formGroupExampleInput2")
      profesor = forms.CharField(label="formGroupExampleInput3")
      cupo = forms.IntegerField(label="formGroupExampleInput4")