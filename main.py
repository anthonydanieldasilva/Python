from clientes.clientes import Clientes


print('______________________________________________________________________\n')
print('_______________________FERIA FRANCA / CoderHouse _____________________\n')
print('______________________________________________________________________\n')

print('INGRESA TU OPCION :\nPARA PANEL DE USUARIOS, PRECIONA 1\nPARA PANEL DE COMPRAS, PRECIONA 2\n')

opcion_ingresada = int(input('! ingresa la opcion! : '))

if opcion_ingresada == 1 or opcion_ingresada ==2:

    if opcion_ingresada == 1:

        print("BIENVENIDO AL PANEL DE USUARIOS\n")
        print('PARA DARTE DE ALTA PRECIONA (1\nPARA INGRESAR A TU PERFIL PRECIONA (2\n')

        opcion_registro_O_login = int(input('! ingresa la opcion! : '))

        if opcion_registro_O_login == 1:

            print("BIENVENIDO AL REGISTRO DE CLIENTES\n")
            print("Ingrea tu nombre y un passwod Y unos datos  mas de elevancia para identificarte:\n")
        
            nombre_cliente = input("Tu nombre: ")
            password_cliente = input("elige un PassWord: ")
            direccion_cliente = input("Tu direccion: ")
            telefono_cliente = input("El numero de tu celular: ")

            def Registro_cliente ():

                NUEVO_CLIENTE = Clientes(nombre_cliente,password_cliente, direccion_cliente, telefono_cliente)
                NUEVO_CLIENTE.Registro_cliente(nombre_cliente,password_cliente, direccion_cliente, telefono_cliente)
        
        elif opcion_registro_O_login == 2:

            print("PARA ACCEDER: Ingresa tu Nombre Y password acontinuacion\n")
            
            nombre_cliente = input("Nombre: ")
            password_cliente = input("PassWord: ")

            def Ingreso_cliente ():
                LOGIN_CLIENTE = Clientes(nombre_cliente,password_cliente)
                LOGIN_CLIENTE.Ingreso_cliente(nombre_cliente,password_cliente)
                
    elif opcion_ingresada == 2:

        codigoAuto = input("Codigo Auto: ")
        nombreAuto = input("Nombre Auto: ")
    
        ruedas = input("Cantidad ruedas: ")
        puertas = input("Cantidad puertas: ")
        tipo = input("Tipo de auto: ")

        codigoMotor = input("Codigo Motor: ")
else:
    print("! ERROR !  opcion fuera de rango ... reintente")