hobbit1=input("introduce el nombre de nuestro primer hobbit: ")
edadHobbit1=int(input("introduce la edad de nuestro primer hobbit: "))
hobbit2=input("introduce el nombre de nuestro segundo hobbit: ")
edadHobbit2=int(input("introduce la edad de nuestro segundo hobbit: "))
hobbit3=input("introduce el nombre de nuestro tercer hobbit: ")
edadHobbit3=int(input("introduce la edad de nuestro tercer hobbit: "))
puedeRepetir=True
mayordeEdad1=edadHobbit1>=33
mayordeEdad2=edadHobbit2>=33
mayordeEdad3=edadHobbit3>=33
print("pueden repetir?")
if not mayordeEdad1:
    (f"{hobbit1} "+str(puedeRepetir))
    if puedeRepetir:
        repites1=hobbit1
elif not mayordeEdad2:
    print(f"{hobbit2} "+str(puedeRepetir))
    if puedeRepetir:
        repites1=hobbit2
elif not mayordeEdad3:
    print(f"{hobbit3} "+str(puedeRepetir))
    if puedeRepetir:
        repites1=hobbit3
sumaEdad=edadHobbit1+edadHobbit2+edadHobbit3
print("La suma de las edades de los 3 hobbits es: " +str(sumaEdad))
print("¿Pueden repetir?")
if sumaEdad%2==0:
    print(f"{hobbit1} "+str(puedeRepetir))
    if puedeRepetir:
        repites=hobbit1
elif sumaEdad%3==0:
    print(f"{hobbit2} "+str(puedeRepetir))
    if puedeRepetir:
        repites=hobbit2
elif sumaEdad%5==0:
    print(f"{hobbit3} "+str(puedeRepetir))
    if puedeRepetir:
        repites=hobbit3
print("los hobbits que aqui repiten son " +str(repites1) + " y "  +str(repites))







