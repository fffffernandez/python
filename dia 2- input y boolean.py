# El input recoge el dato y lo guarda en nombre.
nombre= input ("introduce tu nombre:")
print ("Hola" + nombre)

# Existen dos tipos de =s en programación:
#   =   -> Asigna lo que hay a la izquierda a lo que hay a la derecha.
#           lo que hay a la derecha
#           Ej. Número = 5
#   ==  -> Es un igual LÓGICO. ¡Compara los valores de tiene de izq a derecha

#           Devuelve true, si son iguales; o false, si son distintas.

#1. Entrada: Numero. Salida: True si es mayor de edad.
# input siempre guarda el valor introducido como str. Si queremos que sea un int
# hay que transformarlo. int (input)...))
numero= int (input("introduce tu edad:"))
#Para saber el tipo -> print (type(numero))
print ("¿Es mayor de edad?")
# Se puede escribir 'esMayorEdad = >= 18'
esMayorEdad = (edad >= 18)
print (esMayorEdad)
#esMayorEdad es de tipo bool.
print (type (esMayorEdad))
print (numero >= 18)

 
