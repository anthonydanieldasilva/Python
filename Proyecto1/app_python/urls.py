from django.urls import path
from app_python.views import Main_page, info , clientes, productos, contacto

urlpatterns = [
    path('inicio/',Main_page, name="inicio"),
    path('clientes/',clientes, name="clientes"),
    path('productos/',productos, name="productos"),
    path('info/',info, name="info"),
    path('contacto/',contacto , name="contacto"),
]
