# Desafio 5 - Control de Vehiculos

tiraronBasura=0
multados=0
cond=0
vehiculos=0
preg="n"

while(preg=="n"):
    print("Ingrese patente: (AAA33301)")
    patente=input()
    if(len(patente)<8):
        print("Datos incorrectos")
        continue
    elif((patente[6]!="1" and patente[6]!="0") or (patente[7]!="1" and patente[7]!="0")):
        print("Datos incorrectos")
        continue
    vehiculos+=1

    if(patente[6]=="1"):
        tiraronBasura+=1

    if(patente[7]=="1"):
        multados+=1

    if(patente[6]=="1" and patente[7]=="1"):
        cond+=1
    
    print("Desea salir? (s/n)")
    preg=input()

print(vehiculos, "fueron observados")
print(tiraronBasura, "han tirado basura")
print(cond, "ya habian sido multados")