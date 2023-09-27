nota = int(input("Introduce tu nota: "))
print ("¿Qué nota tiene? ")
# Si no asumimos una nota válida.
if nota > 10 or nota < 0:
    print ("No es una nota válida")
# Si asumimos una nota válida:
#       'if nota <= 10 and nota >=9:'
elif nota >= 9:
    print("sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print ("Suficiente")
else:
    print ("Suspenso")
