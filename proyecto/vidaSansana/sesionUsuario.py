from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class sesionUsuario(View):
    def __init__(self,request):
        self.request = request
        self.session = request.session
        usuario = self.session.get('usuario')
        self.usuario = usuario
    def get(self,request):
        form = UserCreationForm()
        return httpsResponse(request,{'form':form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        usuario = form.save()
        login(request,usuario)
        return redirect('inicio')