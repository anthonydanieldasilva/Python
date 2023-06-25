from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola")

def segundaVista(request):
    return HttpResponse("<br> holaaaaa <br>")