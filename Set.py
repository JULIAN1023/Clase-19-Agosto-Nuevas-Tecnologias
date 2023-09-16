#los Set son Conjuntos!

#los conjuntos son inmutables, son desordenados ya que no son indexados
#No permite duplicados !!


vocales = {"a", "e", "i","o", "u"}
print(len(vocales))

#Para recorrer los conjuntos se usa in

for i in vocales:
    print(vocales)
print("-------")
for i in vocales:
    print(vocales)    

# tienen el metodo add y el metodo remove, asi que no son tan inmutables como una tupla

vocales.add("@")

for i in vocales:
    print(vocales)

#podemos remover con el metodo remove

vocales.remove("@")

for i in vocales:
    print(vocales)

