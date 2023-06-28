from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    apellido_cliente = models.CharField(max_length=40)
    direccion_cliente = models.CharField(max_length=40)
    telefono_cliente = models.CharField(max_length=40)


class Productos(models.Model):
    codigo_producto = models.CharField(max_length=30)
    nombre_producto = models.CharField(max_length=30)

class Poveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=40)
    password_proveedor= models.CharField(max_length=40)
    direccion_proveedor = models.CharField(max_length=40)
    telefono_proveedor = models.CharField(max_length=40)



# clase a prueba futura para maneja de compras
class CarroCompras(models.Model):
    codigo_compra = models.CharField(max_length=30)
    cantidad_items = models.CharField(max_length=30)
    producto = models.CharField(max_length=30)
    total = models.CharField(max_length=30)
# clase a prueba futura para maneja de compras