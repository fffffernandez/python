import random
minEscaleras=50
maxEscaleras=150
numeroEscaleras=random.randrange(minEscaleras,maxEscaleras+1)
print(f"El numero de escaleras que tengo es {numeroEscaleras}")
PisoEscaleras=1
while PisoEscaleras<=numeroEscaleras:
    if PisoEscaleras%13==0:
        print(f"no pises el escalon {PisoEscaleras}")
    PisoEscaleras+=1

for numeroVueltas in range(5,0,-1):
    print(f"quedan {numeroVueltas} vueltas por dar")

numeroVueltas=5
while numeroVueltas>=0:
    print(f"quedan {numeroVueltas} vueltas por dar...")
    numeroVueltas-=1


contraseña=input("inserte su contraseña: ")
contraseñaCorrecta=contraseña=="ARAÑA"
if contraseñaCorrecta:
    print("¡Puede comenzar tu aventura!")
while not contraseñaCorrecta:
    print("Contraseña incorrecta")
    contraseña=input("inserte su contraseña: ")
    contraseñaCorrecta=contraseña=="ARAÑA"
    if contraseñaCorrecta:
        print("¡Puede comenzar tu aventura!")
    
       





    
        
        


