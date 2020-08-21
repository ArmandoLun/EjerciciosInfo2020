# Desafio 4 - Recetas ecologicas

# IC: Tomate - berenjena
# R1: Lentejas - Apio
# R2: Morron - Cebolla

print("Que receta desea preparar?")
print("1: Receta 1\n2: Receta 2")
receta=int(input())
if(receta==1):
    print("ingrese 3 ingredientes")
    print("Tomate - Berenjena - Apio - Lentejas")
    ing1= input()
    ing2= input()
    ing3= input()
elif(receta==2):
    print("ingrese 3 ingredientes")
    print("Tomate - Berenjena - Morron - Cebolla")
    ing1= input()
    ing2= input()
    ing3= input()
else:
    print("Numero invalido")

if(receta==1):
    print("Usted eligio: Receta 1:")
    print("Con los ingredientes:", ing1+", "+ing2+" y "+ing3)