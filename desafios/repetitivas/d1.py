# Desafio 1 - Aplicacion movil

usuario="juan"
password="soyjuan"
us=""
pw=""
intentos = 0

while(intentos!=4):
    if(us != usuario and pw != password):
        print("Ingrese sus credenciales")
        print("Usuario")
        us=input()
        print("Contraseña")
        pw=input()

        if(us == usuario and pw == password):
            print("Acceso correcto")
            intentos=4
        else:
            print("Datos incorrectos")
            intentos=intentos+1