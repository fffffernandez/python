#Funciones.
# num1, num2 y num3 son argumentos de entrada.
def mediaTresNumeros(num1,num2,num3):
    resultado = (num1,num2,num3)/3
    return resultado
# Podemos tener funciones sin return.
#Esto es una excepcion, de normal no usamos
#   Print() en funciones, solo cuando el objetivo de la función sea mostrar algo.
def dibujarLinea(forma): # forma = "="
    print(forma*20)
def dibujarLineaPuntos(): # sin parametros de entrada.
    print(".")
#Para hacerlo sin print():
def crearLinea(forma):
    return forma*20
#-------------------------------------------------------------------------------
# Código principal - MAINç
dibujarLinea("o")
print ("Probando función")
a = 1
b = 2
c = 3
media = mediaTresNumeros
#dibujarLinea("=")
#dibujarLinea("x")
#dibujarLinea("_")
#dibujarLineaPuntos()
# print() de lo que devuelve la funcion ->
#   Para no hacer print() dentro...
print(crearLinea("O")) 


#00000000000000000000
# Linea hecha con o
#"La media de 5, 10 y 15 es: 10"
#OOOOOOOOOOOOOOOOOOOOO
