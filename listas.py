#CREA UNA LISTA DE LA COMPRA DE 5 INGREDIENTES
ListaIngredientes=[]
numIgredientes=5
contador=0
for ingrediente in range(numIgredientes):
    nombreIngrediente=input("Dime un ingrediente: ")
    ListaIngredientes.append(nombreIngrediente)
for ingrediente in ListaIngredientes:
    print(ingrediente)
for ingrediente in ListaIngredientes:
    contador=contador+1
    print(contador)
    #ejercicios de listas de celia del 1 al 5
    #ejercicio de enunciados el de monstruos.
    #dibujar un cuadrado en el que nos pregunte cuanto va a medir un cuadrado.(o con for o while)


