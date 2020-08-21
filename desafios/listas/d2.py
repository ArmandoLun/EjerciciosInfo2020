#Desafio 2 - Contaminacion de mares

factores = ("productos quimicos", "plasticos", "metalicos")
preg=1

while(preg!=0):
    preg=int(input("Ingrese un numero: "))
    if(preg>0 and preg>=len(factores)):
        print("Numero erroneo")
    elif(preg>0 and preg<len(factores)):
        print(factores[preg])