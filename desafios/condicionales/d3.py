# Desafio 3 - Calculo de fertilizantes

print("Ingrese el tamaño de su terreno (ha)")
terreno = float(input())

print("Ingrese cantidad de compuesto (ha)")
compuesto = float(input())

print("Su terreno tiene vegetacion de tipo matorral? (si / no)")
tieneMatorral = input()

if(tieneMatorral=="no" and compuesto>=terreno*0.1):
    print("Usted puede utilizar fertilizantes")
else:
    print("Usted no puede utilizar fertilizantes")