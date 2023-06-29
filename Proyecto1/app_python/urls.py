from django.urls import path
from django.contrib.auth.views import LogoutView
from app_python.views import Main_page, productos, clientes, info ,contacto, addcliente, viewcliente, serchcliente,loginWeb,registro

urlpatterns = [
    path('inicio/',Main_page, name="inicio"),
    path('clientes/',clientes, name="clientes"),
    path('productos/',productos, name="productos"),
    path('info/',info, name="info"),
    path('contacto/',contacto , name="contacto"),
    path('addcliente/',addcliente , name="addcliente"),
    path('viewcliente/',viewcliente , name="viewcliente"),
    path('serchcliente/',serchcliente , name="serchcliente"),
    path('login/',loginWeb , name="login"),
    path('registro/',registro , name="registro"),
    path('logout/',LogoutView.as_view(template_name = 'app_python/inicio.html') , name="logout"),  
 ]
