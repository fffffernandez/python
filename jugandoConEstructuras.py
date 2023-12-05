import random
#lista VS maps
listaLenguajesProgramacion=["JavaScript","python","java","c#","php","c/c++"]
diccionarioLenguajesProgramacion={0:"JavaScript",1:"python",2:"java",3:"c#",4:"php",5:"c/c++"}
print(f"El lenguaje de programación mas usado es: {listaLenguajesProgramacion[0]}")
print(f"El lenguaje de programación mas usado es: {diccionarioLenguajesProgramacion[0]}")

dicAlumnos={"Mari":32,"Elisa":21,"Angel":22,"Pascual":19}
#Podemos sumarle 1 porque, aunque la clave es "Mari", el valor es un int.
print(f"Mari tiene {dicAlumnos['Mari']*3} años")

print(f" diccionario de alumnos: {dicAlumnos}")
print(f"Lista de alumnos disponibles en el diccionario: {list(dicAlumnos)}")

print("Iprimimos el diccionario de alumnos en un bucle for: ")
for elemento in dicAlumnos:
    print(elemento)
print("Imprimimos los valores del diccionario de alumnos en un bucle for: ")
for elemento in dicAlumnos:
    print(dicAlumnos[elemento])

print("El nombre de los alumnos que tienen mas de 30 años: ")
for elemento in dicAlumnos:
    if dicAlumnos[elemento]>=30:
        print(elemento)
dicAlumnos["Lucia"]=23
print(f"Lista de alumnos disponibles en el diccionario: {list(dicAlumnos)}")
alumEliminado=dicAlumnos.pop("Lucia")
print(f"El diccionario de alumnos: {dicAlumnos}")

#Aleatorios

valorAleatorio = random.choice(listaLenguajesProgramacion)
print(f"el lenguaje aleatorio es: {valorAleatorio}")