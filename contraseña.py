#Crea un programa que pregunte que contraseña quiero poner y que despues el programa la pregunte de nuevo
# hasta que no la escriba igual no se cierra
contraseña=input("Dime una contraseña: ")
contraseñaVerificacion=""
Oportunidades=4
while Oportunidades>0 and not contraseña==contraseñaVerificacion:
    contraseñaVerificacion=input("Repite tu contraseña: ")
    if contraseña==contraseñaVerificacion:
        print("Contraseña correcta, acceso concedido")
    else:
        print("Lo siento, contraseña incorrecta.")
        Oportunidades=Oportunidades-1
        print(f"tienes {Oportunidades} intentos")
        if Oportunidades==0:
            print("Acceso denegado, has intentado entrar demasiadas veces, intentelo de nuevo en 3 horas.")
            
