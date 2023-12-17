import time
dinero=500
print("Tengo 500€")
contadorPrestamos=0
while not dinero<=0:
    DineroPrestar=int(input("¿Cuánto dinero me puedes prestar?: "))
    if DineroPrestar>dinero:
        print(f"Lo siento, no puedo dejarte {DineroPrestar}€. Puedo prestarte {dinero}€.")
        dineroRestante=dinero-dinero
        print(f"Me queda {dineroRestante}")
    else:
        contadorPrestamos+=1
        dinero-=DineroPrestar
        print(f"He hecho {contadorPrestamos} prestamos")
        print(f"Me queda {dinero}€")
        print(f"He hecho {contadorPrestamos} prestamos")
    if dinero==0 or dineroRestante==0:
        print("No me queda dinero para prestar.")
cronometrorRelojOTemporizador=input("¿Quieres un cronometro, un temporizador o un reloj?: ")
if cronometrorRelojOTemporizador=="cronometro":
    horas=0
    minutos=0
    segundos=0
elif cronometrorRelojOTemporizador=="reloj":
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

if cronometrorRelojOTemporizador=="temporizador":
    horas=24
    minutos=60
    segundos=60
    horasQ=int(input("Que hora quieres: "))
    minutosQ=int(input("Que minuto quieres:"))
    segundosQ=int(input("Cuantos segundos quieres poner: "))
while segundos<=0 and minutos<=0 and horas<=0:
    segundos=segundos-1
    if segundos==0:
        minutos=minutos-1
        segundos=0
        if minutos==0:
            horas=horas-1
            minutos=0
    print(f"{horas}:{minutos}:{segundos}")
    time.sleep(1)
    