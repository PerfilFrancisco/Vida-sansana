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
    path('crearT/',views.crearTaller,name='crear_taller'),
    path('',views.inicio,name='inicio'),
    path('publicacion/',views.crearPublicacion,name='crear_publicacion'),
    path('login/',views.loguear,name='login'),
    path('carrusel/',views.carrusel,name='carrusel'),
    path('inscribir/',views.inscribir,name='inscribir'),
    path('puntuar/',views.puntuar,name='puntuar'),
    path('previa/',views.previa,name='previa'),
]
