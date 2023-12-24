"""1.-
Crea una lista de 5 palabras directamente en el código.


2.-
Crea una lista de 5 palabras, solicitándolas por consola.

3.-
Solicita de cuántas palabras quieres que sea una lista.
Crea una lista de ese número de palabras, solicitándolas por consola.

4.-
Crea una lista que contenga los números del 1 al 20

5.-
Solicita dos números por consola.
Crea una lista que contenga los números comprendidos entre esos dos, ambos incluidos.
Asegurate de que funcione aunque el primer numero introducido sea menor que el primero."""

#1
lista5Palabras=["casa","mansión","ratón","teclado","pantalla"]
print(lista5Palabras)
#2
Lista5Solicitando=[]
numPalabras=5
for palabras in range (numPalabras):
    nombrePalabra=input("Dime una palabra: ")
    Lista5Solicitando.append(nombrePalabra)
print(Lista5Solicitando)
#3
ListaPalabras=[]
numPalabrass=int(input("¿Cuántas palabras quieres que tenga la lista?: "))
for palabras in range (numPalabrass):
    nombrePalabraLista=input("Dime una palabra: ")
    ListaPalabras.append(nombrePalabraLista)
print(ListaPalabras)
#4
lista1Al20=[]
numnum=20
for lista1Al20 in range(1,20):
    print(lista1Al20)
#5
lista=[]
numero1=int(input("Dime un número: "))
numero2=int(input("Dime otro número: "))
for num in range(numero1, numero2):
    lista.append(num)
for num in range(numero2, numero1):
    lista.append(num)
print(lista)