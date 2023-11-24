""" # _INSTRUCCIONES_
# _Los mensajes "..." pueden personalizarse. Siéntete libre de añadir todo el lore que quieras.
# _¿Ves funciones dónde no las hay? Hazlas, seguramente mejoren tu código. 

# Ejercicios input/print
#0. Solicita por teclado un color. Guardalo para más tarde.
print("el congreso estuvo divertido, de que color era la chaqueta de la chica fantasia?")
color=input()

color=input("el congreso estuvo divertido, de que color era la chaqueta de la chica fantasia?")

#1. Solicita por teclado una palabra e imprimela de nuevo. 
print("dime una palabra: ")
palabra=input()
print("la palabra que has guardado en el programa es " + 2*palabra)
#2. Solicita por teclado una palabra y repítela 5 veces.
print(5*palabra)
#3. Solicita por teclado una palabra y repítela 5 veces separándola por espacios.
#return (f"{palabra} :")
print(5*(palabra+" y "))
#4. Solicita una palabra y un número. Repite la palabra tantas veces como indique el número.
print("dime una palabra: ")
palabra=input()
numero=int(input("dime un numero: "))
print((numero)*(palabra+" , "))

#5. Solicita una palabra y un número. Muestra por pantalla: "Tengo <numero> <palabra>s".
print("el numero de "+ palabra + " que tengo es " + str(numero))
print("Tengo "+ str(numero) + " " +palabra)
"""
# Ejercicios operadores.
#6. Solicita por teclado un número y multiplícalo por 0.
print("dame un numero: ")
numero=int(input())
resultado= numero*0
print(numero*0)
numeroASumar=int(input("dime un numero para sumarle al calculo que hemos realizado. "))
resultado=resultado+numeroASumar
resultado= 8
print(resultado)


#7. Solicita por teclado dos números y multiplícalos entre sí.
print("Dame dos numeros: ")
numero1=int(input())
numero2=int(input())

numero1=int(input("dime un numero: "))
numero2=int(input("dime otro numero: "))
print("Vamos a multiplicar los dos numeros que me digas entre si")
print(numero1*numero2)
resultado=numero1*numero2
print("el resultado de la multiplicacion es " +str(resultado))
print("el resultado de la multiplicacion es ")
print(resultado)

#8. Solicita por teclado dos números y escribe true si el primero es mayor.
esMayor=numero1>numero2
esMenor=numero1<numero2
print(esMayor)
print(esMenor)
esMayorOIgual=numero1>=numero2
print(esMayorOIgual)
# 8.1 Haz un booleano que imprima true si el resultado es mayor que numero1
print("Vamos a ver si el resultado es mayor que el primer numero. ")
esMayor=resultado>numero1
print(esMayor)
#9.0. Solicita por teclado un número y escribe true si es par
print("vamos a ver si el resultado del calculo anterior es par. ")
esMayor=resultado%2
print(esMayor)
esMayor=resultado%2 == 0
print(esMayor)

#9.1. Solicita por teclado un número y escribe true si es multiplo de 5.
print("vamos a ver si el resultado del calculo anterior es multiplo de 5. ")
esMultiploDe5=resultado%5 == 0
print(esMultiploDe5)
print("vamos a ver si un numero es multiplo de 5. ")
numero=int(input("dime un numero: "))
esMultiploDe5=numero%5 == 0
print(esMultiploDe5)

# Ejercicios booleanos - condicionales.
#10. Solicita por teclado dos numeros y la palabra 'suma' o 'resta'. Realiza la operación correspondiente.


#11. Solicita por teclado dos numeros. Escribe "El primer número es mayor" o "El primer número es menor" segun corresponda.
#12. Solicita por teclado dos numeros. Escribe "Has ganado" si el segundo número menos el primero da un valor positivo.
#13. Solicita por teclado un color. Si coincide con el color del ejercicio #0 escribe "¿Cómo sabías que era mi color favorito?"


#14. Solicita por teclado un día de la semana y un número. Si el número coincide con su día de la semana o el día introducido es viernes escribe "¡Has ganado!"
#15. Solicita por teclado tres números. Si los dos primeros son mayores que el tercero, escribe "Mayores"; si los dos son menores que el tercero, escribe "Menores"; para cualquier otro caso, escribe "¿Iguales?"
