from clientes.clientes import Clientes

class Compras (Clientes):
    def __init__(self, codigo_compra=None, cantidad_items=None, producto=None, total=None):
        self.codigo_compra = codigo_compra
        self.cantidad_items = cantidad_items
        self.producto = producto
        self.total = total

    def Ver_compras (self,codigo_compra,):
        with open('./recursos/listado_compras','r') as listado_compras:
            for detalle in listado_compras:
                detalle_compras = listado_compras.split("|")
                if codigo_compra == detalle_compras[1]:
                    print(detalle)
                    return(detalle_compras)
            else:
                listado_compras.close()
                return False

