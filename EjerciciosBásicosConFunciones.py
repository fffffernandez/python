
   


# _INSTRUCCIONES_
# _Los mensajes "..." pueden personalizarse. Siéntete libre de añadir todo el lore que quieras.
# _¿Ves funciones dónde no las hay? Hazlas, seguramente mejoren tu código. 

# Ejercicios input/print
#0. Solicita por teclado un color. Guardalo para más tarde.
def solicitarColor():
    color=input("dime un color: ")
    return color
solicitarColor()
color=solicitarColor()
print(color)
print("el congreso estuvo divertido, de que color era la chaqueta de la chica fantasia?")
color=input()

color=input("el congreso estuvo divertido, de que color era la chaqueta de la chica fantasia?")

#1. Solicita por teclado una palabra e imprimela de nuevo.
def solicitaPalabra():
    palabra=input("dime una palabra: ")
    return palabra
palabra=solicitaPalabra()
print(palabra) 
print("dime una palabra: ")
palabra=input()
print("la palabra que has guardado en el programa es " + 2*palabra)
#2. Solicita por teclado una palabra y repítela 5 veces.
print(5*palabra)
#3. Solicita por teclado una palabra y repítela 5 veces separándola por espacios.
#return (f"{palabra} :")
print(5*(palabra+" y "))
#4. Solicita una palabra y un número. Repite la palabra tantas veces como indique el número.
def solicitaNumero():
    numero=int(input("dime un numero: "))
    return numero
palabra=solicitaPalabra()
numero=solicitaNumero()
print("la palabra es " +palabra*numero)



#5. Solicita una palabra y un número. Muestra por pantalla: "Tengo <numero> <palabra>s".
palabra=solicitaPalabra()
numero=solicitaNumero()
print(f"tengo {numero} {palabra}s")

# Ejercicios operadores.
#6. Solicita por teclado un número y multiplícalo por 0.
def numeroPor0(num):
    resultado=num*0
    return resultado

numero=solicitaNumero()
print(numeroPor0(numero))

#7. Solicita por teclado dos números y multiplícalos entre sí.
def multiplica2Num(num,num2):
    resultado=num*num2
    return resultado
numero=solicitaNumero()
numero2=solicitaNumero()
print(multiplica2Num(numero, numero2))

#8. Solicita por teclado dos números y escribe true si el primero es mayor.
numero=solicitaNumero()
numero2=solicitaNumero()
def esMayor(num1,num2):
    primerNumeroMayor=num1>num2
    return primerNumeroMayor
numeroMayor=esMayor(numero,numero2)
print(numeroMayor)
# 8.1 Haz un booleano que imprima true si el resultado es mayor que numero1



#9.0. Solicita por teclado un número y escribe true si es par
numero=solicitaNumero()
def numeroPar(num):
    esPar=num%2==0
    return esPar
par=numeroPar(numero)
print(par)



#9.1. Solicita por teclado un número y escribe true si es multiplo de 5.
numero=solicitaNumero()
def numeroMult5(num):
    multiplo5=num%5==0
    return multiplo5
mult5=numeroMult5(numero)
print(mult5)



#un programa que m pregunte el dinero que tengo
#que pregunte el precio del objeto
#que saque el dinero  que me quedaria al comprar el objeto.

# Ejercicios booleanos - condicionales."""

# Ejercicio 10 11 12 y 13 sin booleanos (ej If num>0: es positivo)

#10. Solicita por teclado dos numeros y la palabra 'suma' o 'resta'. Realiza la operación correspondiente.
numero=solicitaNumero
numero2=solicitaNumero
sumarRestar=input("Quieres sumar o restar?: ")
def sumaResta(numero,numero2):
    if sumarRestar=="sumar":
        print(f"{numero}+{numero2}")
    elif sumarRestar=="restar":
        print(f"{numero}-{numero2}")
    return sumarRestar
print(sumaResta)

    

    

#11. Solicita por teclado dos numeros. Escribe "El primer número es mayor" o "El primer número es menor" segun corresponda.

#12. Solicita por teclado dos numeros. Escribe "Has ganado" si el segundo número menos el primero da un valor positivo.

#13. Solicita por teclado un color. Si coincide con el color del ejercicio #0 escribe "¿Cómo sabías que era mi color favorito?"


#14. Solicita por teclado un día de la semana y un número. Si el número coincide con su día de la semana o el día introducido es viernes escribe "¡Has ganado!"


#15. Solicita por teclado tres números. Si los dos primeros son mayores que el tercero, escribe "Mayores"; si los dos son menores que el tercero, escribe "Menores"; para cualquier otro caso, escribe "¿Iguales?"
