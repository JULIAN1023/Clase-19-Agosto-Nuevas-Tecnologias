usuario = {"nombre" : "pepito", "apellido" : "perez", "edad" : 25}
print(usuario)

print(usuario.keys())#es el metodo para que muestre las keys de el diccionario

print(usuario.values())#es el metodo para mirar que valores se agregaron 

print(len(usuario))#para conocer el tamaño del diccionario se usa el metodo len()

print(type(usuario))#metodo type para saber si es una lista o tupla o diccionario

print(usuario.get("nombre"))#cuando queremos buscar un item especifico, podemos uar la funcion get 

#manera 2:
print(usuario["edad"])

usuario["correo"]="pepitop@gmail.com"#para agregar un nuevo item     
print(usuario.get("correo"))

#para actualizar un valor

usuario.update({"correo":"ppepito@gmail.com"})
print(usuario.get("correo"))

#para remover un valor

#usuario.pop("nombre")
#print(usuario.keys())

#para remover el ultimo item insertado

#usuario.popitem()
#print(usuario.keys())

#potra opcion para eliminar

#del usuario["edad"]
#print(usuario.keys())

#para recorrer las keys o los values o recorrer ambos

#ambos con ciclo for

for x,y in usuario.items():
    print(x,y)

#keys

for y in usuario:
    print(y)

#values

for x in usuario.values():
    print(x)

#Podemos crear un diccionario de diccionarios

usuarios = {"usuario1" :{"nombre":"juan","edad":12}, "usuario2":{"nombre":"maria","edad":15}, "usuario3":{"nombre":"julia", "edad":18}}

estudiante1 = {"nota1":4.5, "nota2":4.3}
estudiante2 = {"nota1":4.4, "nota2":4.3}
estudiante3 = {"nota1":4.1, "nota2":4.3}

estudiantes = {
    "estudiante1":estudiante1,
    "estudiante2":estudiante2,
    "estudiante3":estudiante3,
}

print(estudiantes["estudiante2"]["nota2"])

