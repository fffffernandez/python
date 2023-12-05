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

# 1 Crear dos Pokemon: Introduce por teclado el nombre,  
# tipo y nivel de poder de dos pokemons.
# Los tipos disponibles son ‘Agua’, ‘Fuego’ o ‘Planta’. 
# El poder debe ser un valor comprendido entre 0 y 50.

nombrePoke1 = input("Introduce el nombre de un pokemon: ")
tipoPoke1 = input("Introduce el tipo del pokemon: ")
nivelPoke1 = int(input("Introduce el nivel del pokemon: "))

if nivelPoke1 < 0:
    nivelPoke1 = 0 
elif nivelPoke1 > 50:
    nivelPoke1 = 50

nombrePoke2 = input("Introduce el nombre de un pokemon: ")
tipoPoke2 = input("Introduce el tipo del pokemon: ")
nivelPoke2 = int(input("Introduce el nivel del pokemon: "))

if nivelPoke2 < 0:
    nivelPoke2 = 0 
elif nivelPoke2 > 50:
    nivelPoke2 = 50

# 2 Empieza la batalla: ¿Quién ganaría la batalla entre los dos 
# pokemons introducidos?
# Si los tipos son iguales: Gana el que tenga más nivel.
# Si los tipos son distintos: Gana ‘Fuego’ a no ser que el nivel 
# del otro pokemon supere en 10 puntos o más el nivel del pokemon 
# de ‘Fuego’. Si no hay fuego  gana el primer pokemon.

# Versión 8: 
ganador = "NADIE GANA"
# Si los tipos son iguales:
if tipoPoke1==tipoPoke2:
    # Si Poke1 tiene más nivel o igual: Gana Poke1.
    if nivelPoke1>=nivelPoke2:
        ganador = nombrePoke1
    # Si Poke2 tiene más nivel: Gana Poke2.
    else:
        ganador = nombrePoke2
#Si los tipos son distintos:
else: # tipoPoke1!=tipoPoke2
    if tipoPoke1=="Fuego":
        if nivelPoke2-nivelPoke1<=10:
            ganador = nombrePoke1
        else:
            ganador = nombrePoke2
    elif tipoPoke2=="Fuego":
        if nivelPoke1-nivelPoke2<=10:
            ganador = nombrePoke2
        else:
            ganador = nombrePoke1
    else:
        ganador = nombrePoke1

    # Si hay fuego: Gana Fuego a no ser que el nivel del otro sea mayor en 10 puntos.
    # Si no hay fuego: Gana el primero



# 3 Ganador: Imprime por pantalla el nombre del ganador seguido
# de una frase aleatoria. ¿Cómo se genera la frase aleatoria? 
# Llamando a la función fraseAleatoria(), que devuelve un string. 
# No hace falta entender cómo funciona internamente fraseAleatoria(),
# simplemente copia la definición de la función en tu código 
# [sin olvidar el import random].

ganador = nombrePoke1
# "fraseAleatoria" -> String: Literalmente.
# fraseAleatoria -> Variable.
# fraseAleatoria() -> Función.
print(ganador)
print(fraseAleatoria())

# 4 Batalla justa: Determina si la batalla fue justa o no mediante 
# una variable booleana. 
# Si los dos pokemons tenían el mismo tipo la batalla fue justa, 
# si los dos pokemons tienen distinto tipo la batalla no fue justa. 
# Imprime un mensaje que indique si la batalla fue justa o no.

esJusta = tipoPoke1 == tipoPoke2
if esJusta:
    print ("La batalla es justa.")
else:
    print("La batalla no es justa.")