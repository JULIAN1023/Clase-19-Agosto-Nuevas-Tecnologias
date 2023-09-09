#Ejercicio alquiler de bicicletas:
# --se necesita un aplicativo que te de un formulario que te solicite nombre, origen y destino y te genere un numero de tarjeta al azar por cada ingreso (# tarjeta) y que al confrimar estos datos se guarden en una lista llamada "list-prestamos", luego
#   solicite un registro que contenga nombre, apellido, # tarjeta (password), correo, telefono.
#   y estos datos que se ingresen deben quedar guardados en una lista llamada "list-registro".
#   luego acceder a un login que compare el nombre que se digite con los datos que ya esten registrados en la list-registro 
#   y si coinciden los datos que permita abrir un menu que te de dos opciones 1."consulte su informacion" y 2."consulte sus prestamos"
#   eligiendo la opcion 1. el aplicativo debe buscar en la list-registro los datos que coincidan con el nombre que proporcione la persona y si se elige la opcion 2. 
#   debe pedirte tu nombre y si coincide con la lista, debe mostrarte el # tarjeta,  el origen y el destino que estaban en la lista "list-prestamos" correspondiente al nombre digitado.


import random

list_prestamos = []
list_registro = []
login_exitoso = False

def formulario():
    print("\nFORMULARIO PRESTAMO: ")
    nombre = input("Ingrese su nombre: ")
    origen = input("Ingrese su origen: ")
    destino = input("Ingrese su destino: ")
    tarjeta = random.randint(1000, 9999)
    list_prestamos.append({"nombre": nombre, "origen": origen, "destino": destino, "tarjeta": tarjeta})
    print("Su codigo de prestamo es:", tarjeta)

def registro():
    print("\nREGISTRO DE USUARIOS:")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    tarjeta = int(input("Ingrese su codigo de prestamo: "))
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    list_registro.append({"nombre": nombre, "apellido": apellido, "tarjeta": tarjeta, "correo": correo, "telefono": telefono})

def login():
    print("\nLOGIN DE USUARIO:")
    global login_exitoso
    nombre = input("Ingrese su nombre: ")
    for registro in list_registro:
        if registro["nombre"] == nombre:
            login_exitoso = True
            menu()
            return
    print("Nombre no encontrado")

def menu():
    print("MENU CONSULTAS:")
    opcion = int(input("Elija una opción:\n1. Consulte su información\n2. Consulte sus préstamos\n"))
    if opcion == 1:
        consultar_informacion()
    elif opcion == 2:
        consultar_prestamos()

def consultar_informacion():
    nombre = input("Ingrese su nombre: ")
    for registro in list_registro:
        if registro["nombre"] == nombre:
            print("Nombre:", registro["nombre"])
            print("Apellido:", registro["apellido"])
            print("Número de codigo prestamo:", registro["tarjeta"])
            print("Correo electrónico:", registro["correo"])
            print("Número de teléfono:", registro["telefono"])
            return
    print("Nombre no encontrado")

def consultar_prestamos():
    nombre = input("Ingrese su nombre: ")
    for prestamo in list_prestamos:
        if prestamo["nombre"] == nombre:
            print("\n INFORMACION PRESTAMO:")
            print("Número de tarjeta:", prestamo["tarjeta"])
            print("Origen:", prestamo["origen"])
            print("Destino:", prestamo["destino"])
            return
    print("Nombre no encontrado")

formulario()
registro()
login()
if login_exitoso:
    menu()


