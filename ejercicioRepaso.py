#un programa donde de primeras vamos a tener una variable llamada Dinero=500, hacemos un bucle while con una pregunta que dice ¿cuanto dinero me puedes prestar?
#hasta que tengo 0 o x y cuando me quede ese dinero se cerrara ese programa
import time
dinero=500
print("Tengo 500€")
DineroPrestar=0
contadorPrestamos=0
while not dinero<=0:
    DineroPrestar=int(input("¿cuanto dinero me puedes prestar?: "))
    if DineroPrestar>dinero:
        print(f"Lo siento no puedo dejarte ese dinero, pero puedo prestarte {dinero} ")
        dinero=dinero-dinero
    else:
        contadorPrestamos=contadorPrestamos+1
        dinero=dinero-DineroPrestar
    print(f"Me queda {dinero}€")
    print(f"He hecho {contadorPrestamos} prestamos")


cronometroOreloj=input("Q¿Quieres un cronometro o un reloj?: ")
if cronometroOreloj=="cronometro":
    horas=0
    minutos=0
    segundos=0
elif cronometroOreloj=="reloj":
    horas=int(input("Que hora es: "))
    minutos=int(input("Que minutos:"))
    segundos=int(input("Cuantos segundos son: "))
while segundos<=59 and minutos<=59 and horas<=23:
    segundos=segundos+1
    if segundos==59:
        minutos=minutos+1
        segundos=0
        if minutos==59:
            horas=horas+1
            minutos=0
    print(f"{horas}:{minutos}:{segundos}")
    time.sleep(1)
    
    
 
   

    