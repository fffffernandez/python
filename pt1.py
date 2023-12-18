import random

def fraseAleatoria():
    frases = [
        "¡El ganador de la batalla es increible!",
        "¡La victoria ha sido para el mejor Pokémon!",
        "¡Nuestro ganador a triunfado en la batalla!",
        "¡Enhorabuena al Pokémon ganador!",
        "¿Quién ganará la próxima vez?"
    ]
    fraseElegida = random.choice(frases)
    return fraseElegida


pokemon1=input("dime un pokemon: ")
tipoPokemon1=input(f"¿Indiqueme si el tipo de {pokemon1} es Agua, Fuego o Planta: ")
nivelPoder1=int(input(f"¿Indique el nivel de poder de su {pokemon1}: "))
if nivelPoder1<0:
    nivelPoder1=0
elif nivelPoder1>50:
    nivelPoder1=50
pokemon2=input("dime otro pokemon: ")
tipoPokemon2=input(f"¿Indiqueme si el tipo de {pokemon2} es Agua, Fuego o Planta: ")
nivelPoder2=int(input(f"¿Indique el nivel de poder de su {pokemon2}: "))
if nivelPoder2<0:
    nivelPoder2=0
elif nivelPoder2>50:
    nivelPoder2=50
GANADOR="NADIE GANA"
if tipoPokemon1==tipoPokemon2:
    if nivelPoder1>nivelPoder2:
        GANADOR=pokemon1
elif tipoPokemon1==tipoPokemon2:
    if nivelPoder1<nivelPoder2:
        GANADOR=pokemon2
elif tipoPokemon1=="fuego":
    if nivelPoder2<10:
        GANADOR=pokemon1
elif tipoPokemon2=="fuego":
    if nivelPoder1<10:
        GANADOR=pokemon2
else:
    GANADOR=pokemon1

GANADOR=pokemon1
print(f"el ganador de la batalla es " +GANADOR +fraseAleatoria())