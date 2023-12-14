import random
minEscaleras=50
maxEscaleras=150
numeroEscaleras=random.randrange(minEscaleras,maxEscaleras+1)
print(f"El numero de escaleras es {numeroEscaleras}")
escalonesPisados=0
PuertaEntrada=150
while not PuertaEntrada:
    escalonesPisados=escalonesPisados+1
    escalonProhibido=escalonesPisados%13==0
    if escalonProhibido:
        print(f"Tenemos que saltarnos {escalonProhibido}")
        
    

