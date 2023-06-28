from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_python.models import Cliente
from app_python.forms import Form_addcliente


# vistas de html nav #

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

def addcliente ( request ):
    return render (request , "app_python/addcliente.html")

def serchcliente ( request ):
    return render (request , "app_python/serchcliente.html")

def viewcliente ( request ):
    return render (request , "app_python/viewcliente.html")

# vistas de html nav #

# metodos de creacion y busqueda clientes #

def add_clientes( request ):
    if request.method == 'POST':
        cliente = Cliente(nombre_cliente=request.POST["nombre_cliente"],apellido_cliente=request.POST["apellido_cliente"], Dirección=request.POST["Dirección"], telefono_cliente=request.POST["telefono_cliente"])
        cliente.save()  
    else:
       return render(request, "app_python/clientes.html")
    
def serch_cliente(request):
    if request.GET["nombre_cliente"]:
        nombre_cliente = request.GET["nombre_cliente"]
        cliente = Cliente.objects.filter(nombre_cliente = nombre_cliente)
        return render(request, "app_python/clientes.html",)
    else:
        respuesta = "Cliente No hallado"
    return render(request, "app_python/clientes.html")


