#Desafio 1 - Contaminacion

personas=3
respuestas = []
menor=11

for i in range(personas):
    print("Cuanto sabe de contaminacion? Ingrese del 1 al 10")
    resp=int(input())
    respuestas.append(resp)

respuestas.sort()


print(respuestas)