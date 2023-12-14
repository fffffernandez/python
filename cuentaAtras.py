import time
Horas=int(input("¿Que hora quieres?: "))
Minutos=int(input("¿Que minuto quieres?: "))
Segundos=int(input("¿Que segundo quieres?: "))
for hora in range(Horas,0-1,-1):
    for minuto in range(Minutos,0-1,-1):
        for segundo in range(Segundos,0-1,-1):
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(0.1)