acumingresos = 0
acumegresos = 0
saldo = 0

def Ingresos():
    global saldo, acumingresos

    ingresos = int(input("Registre monto de ingreso:"))
    saldo = saldo + ingresos
    acumingresos += 1

    print(f"Su saldo actual es: ${saldo} y a registrado {acumingresos} ingresos.")

def Egresos():
    global saldo, acumegresos

    egresos = int(input("Registre monto a retirar:"))

    if egresos < saldo:
     saldo = saldo - egresos
     acumegresos += 1

     print(f"Su saldo actual es: ${saldo} y sus egresos han sido: {acumegresos}")
    else: 
       print(f"No puede realizar un pago mayor al que posee en su cuenta. Su saldo actual es: ${saldo}")
     

def menu():
   
   opc = int(input("Elije proceso a ejecutar:\n 1. Ingresar:\n 2. Egresos:\n"))

   if opc == 1:
      
      Ingresos()
      menu()

   else:

    if opc == 2:
      
      Egresos()
      menu()


menu()     
  

