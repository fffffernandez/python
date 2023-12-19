#En el zoológico de monstruos hemos visto un montón de criaturas fantásticas.
#Cada vez que alguien veía uno, gritaba el nombreMonstruo! frase! -> "Monstruo! Que feo!" Hemos hecho una lista de todas las veces que ha gritado la gente. 
#Tenemos que sacar de esa lista, otra lista con los tipos de monstruo que hemos visualizado.
GritosGente=["Oso, que feo","Casa, que fea","gato, que feo"]
listaMonstruos=[]
numMonstruos=3
for monstruo in range(numMonstruos):
    nombreMonstruo=input("Dime un monstruo: ")
    if nombreMonstruo=="oso":
        print(f"oso ¡que feo!")
    elif nombreMonstruo=="casa":
        print(f"casa ¡que feo!")
    elif nombreMonstruo=="gato":
        print(f"gato ¡que feo!")
    else:
        print("Que bonito!!")
        print(f"{nombreMonstruo} ¡que feo!")
    listaMonstruos.append(nombreMonstruo)
