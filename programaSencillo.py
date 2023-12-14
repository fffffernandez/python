numeroOvejas=int(input("¿Cúantas ovejas necesitas para dormir?: "))
contador=0
while not contador==numeroOvejas:
    contador=contador+1
    print(f"{contador} ovejas")
print("zzzz")
numeroOvejasFor=int(input("¿Cúantas ovejas necesitas para dormir?: "))
for ovejas in range(numeroOvejasFor,0-1,-2):
    print(f"{ovejas} ovejas")



