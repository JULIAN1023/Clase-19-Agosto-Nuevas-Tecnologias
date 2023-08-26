#La aplicacion debe permitir registrar ingresos y contar el saldo de estos.
#Debe permitir registrar egresos y mostrar el saldo.
#si el egreso es mayor que el saldo, no debe permitir el retiro y mostrara un mensaje de saldo insuficiente.


saldo = 0

acumIngresos=0

acumEgresos=0

isOn= int(input("Ingrese 1 para inicializar la App:"))

while isOn != 0:

    Opc = int(input("1. Ingreso:\n 2. Egreso:\n 3.Salir"))

    if Opc == 1:

        ingreso = int(input("Registre el ingreso:"))

        saldo = saldo + ingreso

        print(f"Su saldo es ${saldo}")

        acumIngresos += 1

        print(acumIngresos)

    elif Opc == 2:

        egreso = int(input("Registre el monto a retirar:"))
        
        saldo = saldo - egreso

        if saldo <= 0:
            print("saldo insuficiente")
            saldo = saldo + egreso
            print(saldo)
            
        else: 
         print(f"su saldo es: ${saldo}")
         acumEgresos+= 1
         print(acumEgresos)

    elif Opc == 3:
       
       print("Salir")
       isOn=0
    else:
       print("Ingrese una opcion valida")

       







 





