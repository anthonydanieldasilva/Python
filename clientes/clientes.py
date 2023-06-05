
class Clientes:

    def __init__(self, nombre_cliente=None, password_cliente=None, direccion_cliente=None, telefono_cliente=None):
        self.nombre_cliente = nombre_cliente
        self.password_cliente = password_cliente
        self.direccion_cliente = direccion_cliente
        self.telefono_cliente = telefono_cliente


    def Registro_cliente (self,nombre_cliente,password_cliente, direccion_cliente, telefono_cliente ):
        with open('./recursos/listado_clientes', 'a') as nuevo_registro:
            data = f'{nombre_cliente}|{password_cliente}|{direccion_cliente}|{telefono_cliente}|\n'
            nuevo_registro.write(data)
            nuevo_registro.close()
        print("Registrado con exito")


    def Ingreso_cliente (self, nombre_cliente, password_cliente ):

        with open('./recursos/listado_clientes', 'r') as ingreso_cliente:
            
            for clientes in ingreso_cliente:
                detalle_cliente = ingreso_cliente.split("|")   

                if (nombre_cliente == clientes[1] and password_cliente == clientes[2]):
                    print(f"! Bienvenido {nombre_cliente} !")
                    print("¿Estas listo para hacer el pedido para este findesemana de feriaFranca?")
                    ingreso_cliente.close()
                    return detalle_cliente
                else:
                    print("!Error! , Hay datos invalidos. Vuelve a intentarlo... ")
                    ingreso_cliente.close()
                    return False

                

    
