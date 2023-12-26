def menorEdad(edad):
    edad<33
    return edad<33
def sumaEdad(edad1,edad2,edad3):
    sumar=edad1+edad2+edad3
    if sumar%2==0:
        print("¡El primer hobbit puede repetir!")
    if sumar%3==0:
        print("¡El segundo hobbit puede repetir!")
    if sumar%5==0:
        print("¡El tercer hobbit puede repetir!")
hobbit1=input("introduce el nombre de nuestro primer hobbit: ")
edadHobbit1=int(input("introduce la edad de nuestro primer hobbit: "))
hobbit2=input("introduce el nombre de nuestro segundo hobbit: ")
edadHobbit2=int(input("introduce la edad de nuestro segundo hobbit: "))
hobbit3=input("introduce el nombre de nuestro tercer hobbit: ")
edadHobbit3=int(input("introduce la edad de nuestro tercer hobbit: "))
puedeRepetir=True
repite1=menorEdad(edadHobbit1)
repite2=menorEdad(edadHobbit2)
repite3=menorEdad(edadHobbit3)
print(f"{hobbit1} puede repetir: {repite1}")
print(f"{hobbit2} puede repetir: {repite2}")
print(f"{hobbit3} puede repetir: {repite3}")

