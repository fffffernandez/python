import time
def tiempoReloj(horas,minutos,segundos):
    pantallaReloj=f"{horas}:{minutos}:{segundos}"
    return pantallaReloj
    

for horas in range (0,60):
    for minutos in range(0,60):
        for segundos in range(0,60):
            print(tiempoReloj(horas,minutos,segundos))
            time.sleep(0.1)

#funcion con el reloj que pase el segundo, minuto la hora en la que se encuentra y luego lo imprima
