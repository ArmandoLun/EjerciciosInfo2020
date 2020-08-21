# Desafio 5 - Barrios de la ciudad

#tipo - nombre

al="abcdefghijkl"
mz="mnopqrstuvwxyz"

print("Ingrese nombre del barrio")
nombre=input()

print("Ingrese tipo de barrio (centrico / no centrico)")
tipo=input()

antm= al.find(nombre[0])
posm= mz.find(nombre[0])

if((tipo=="centrico" and antm>=0) or (tipo=="no centrico" and posm>=0)):
    print("Su barrio pertenece a Seccion A")
else:
    print("Su barrio pertenece a Seccion B")