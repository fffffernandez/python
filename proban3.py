lista=[]
numero1=int(input("Dime un número: "))
numero2=int(input("Dime otro número: "))
for num in range(numero1, numero2+1):
    lista.append(num)
for num in range(numero2, numero1+1):
    lista.append(num)
print(lista)