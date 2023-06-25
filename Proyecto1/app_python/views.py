from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def Main_page ( request ):
    return render (request , "app_python/inicio.html")

def productos ( request ):
    return render (request , "app_python/productos.html")

def clientes ( request ):
    return render (request , "app_python/clientes.html")

def info ( request ):
    return render (request , "app_python/info.html")

def contacto ( request ):
    return render (request , "app_python/contacto.html")

