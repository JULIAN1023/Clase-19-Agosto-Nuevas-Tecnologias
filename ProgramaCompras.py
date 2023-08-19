def registro():
    print("Formulario de registro")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    return usuario, contraseña

def login(datos_registro):
    print("Formulario de login")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == datos_registro[0] and contraseña == datos_registro[1]:
        return True
    else:
        return False

def compras():
    valor_compra = float(input("Valor de la compra: "))
    num_cuotas = int(input("Número de cuotas a pagar: "))
    valor_cuota = valor_compra / num_cuotas
    print(f"El valor de cada cuota es: {valor_cuota}")
    while valor_compra > 0:
        pago = float(input("Ingrese el pago: "))
        if pago == valor_cuota:
            valor_compra -= pago
            num_cuotas -= 1
            print(f"Quedan {num_cuotas} cuotas por pagar")
        else:
            print("El pago no es igual al valor de la cuota")

def menu():
    datos_registro = None
    while True:
        print("Menú")
        print("1. Registro")
        print("2. Login")
        print("3. Compras")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            datos_registro = registro()
        elif opcion == "2":
            if datos_registro is not None:
                if login(datos_registro):
                    print("Login correcto")
                else:
                    print("Login incorrecto")
            else:
                print("Primero debe registrarse")
        elif opcion == "3":
            if datos_registro is not None:
                compras()
            else:
                print("Primero debe registrarse")

menu()
