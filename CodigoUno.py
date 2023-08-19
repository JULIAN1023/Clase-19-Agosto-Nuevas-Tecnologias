Valorcompra = int(input("Digite el valor de su compra: "))
Cuotas = int(input("eliga una cantidad de cuotas: "))


Valorcuotas = Valorcompra / Cuotas

print(Valorcuotas)

Pagocuota = int(input("digite el valor de su pago "))

while Valorcuotas == Pagocuota and Valorcompra != 0:

    Valorcompra-= Valorcuotas
    print(Valorcompra)


