
#las tuplas son inmutables
#contienen distintos tipos de datos
#se diferencian de las listas en que la tupla no se puede añadir ni actualizar ni eliminar datos
#se puede acceder la tupla indicando el indice de la misma, el cual comienza desde 0 al igual que la lista
#para recorrer la tupla usamos un ciclo "for"
#podemos hacer joins entre tuplas
#para conocer el tamaño usamos la funcion len(dias_semanas)
#las tuplas permiten duplicados


dias_semana= ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado" , "domingo")

print(type(dias_semana))

print(dir(dias_semana))

print(len(dias_semana)) #funcion len para saber la cantidad de datos de la  tupla o lista

print(dias_semana[0]) #print para mirar que hay en cada posicion que requieres
print(dias_semana[1])
print(dias_semana[2])

#podemos hacer slicing indicando el rango que queremos imprimir

print(dias_semana[:6])
print(dias_semana[0:])
print(dias_semana[-1:])
print(dias_semana[:-1])

#para recorrer la tupla, utilizamos el ciclo for:

for i in range(len(dias_semana)):
    print(dias_semana[i])


#para cambiar o añadir un valor de la tupla debemos primero convertirla a una lista
    
dias_semana_lista = list(dias_semana)#de esta manera hacemos una tupla en lista
print(type(dias_semana_lista))

dias_semana_lista.append("Festivo")#append es un metodo para añadir un valor en la ultima posicion de la lista
print(dias_semana_lista[:8])

dias_semana_lista.pop() #pop es un metodo para eliminar el ultimo valor de una lista
print(dias_semana_lista[:8])

dias_semana = tuple(dias_semana_lista)#de esta manera volvemos una lista a tupla
print(type(dias_semana))







