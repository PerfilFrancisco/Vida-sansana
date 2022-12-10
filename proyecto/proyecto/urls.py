"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vidaSansana import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscribir/',views.inscribir_taller,name='inscribir'),
    path('',views.inicio,name='inicio'),
    path('publicacion/',views.crearPublicacion,name='crear_publicacion'),
    path('login/',views.loguear,name='login'),
    path('puntuar/',views.puntuar,name='puntuar'),
    path('previa/',views.previa,name='previa'),
    path('talleres/',views.listaTalleres,name='talleres'),
    path('registro/',views.registro,name='registro'),
    path('perfil/',views.perfil,name='perfil'),
    path('lp/',views.lpymes,name='lpymes'),
    path('bl/',views.blg,name='badlog'),
    path('crearTv2/',views.crearTv2,name='crearTv2'),
    path('autores/',views.autores,name='autores'),
]
