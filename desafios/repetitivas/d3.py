# Desafio 3 - Reciclado de tapitas

cerrado="n"

while(cerrado=="n"):
    print("Ingrese importe")
    importe=int(input())

    print("Ingrese tapitas")
    tapitas=int(input())
    desc=""

    if(tapitas>=20):
        desc = "rojo"
    elif(tapitas>=10):
        desc= "amarillo"
    elif(tapitas<10):
        desc= "blanco"

    if(desc=="rojo"):
        importe=importe-importe*0.4

    if(desc=="amarillo"):
        importe=importe-importe*0.25

    print("Total a pagar:", importe)
    print("Desea salir? (s/n)")
    cerrado=input()