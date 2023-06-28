from django import forms

class Form_addcliente (forms.Form):
    nombre_cliente = forms.CharField(max_length=40)
    password_cliente = forms.CharField(max_length=40)
    direccion_cliente = forms.CharField(max_length=40)
    telefono_cliente = forms.CharField(max_length=40)
    
class Productos(forms.Form):
    codigo_producto = forms.CharField(max_length=30)
    nombre_producto = forms.CharField(max_length=30)



# forms a prueba futura para maneja de compras
class CarroCompras(forms.Form):
    codigo_compra = forms.CharField(max_length=30)
    cantidad_items = forms.CharField(max_length=30)
    producto = forms.CharField(max_length=30)
    total = forms.CharField(max_length=30)