def separar(lista):
    mayor100 = []
    menor = []

    for i in range(len(lista)):
        if(lista[i]>100):
            mayor100.append(lista[i])
        else:
            menor.append(lista[i])
    return mayor100, menor

cantArboles = []
continuar = True

while(continuar):
    ciudad =int(input("Cuantos arboles se plantaron en la ciudad?: "))
    cantArboles.append(ciudad)

    preg = input("Desea continuar?: ")
    if(preg == 'n'):
        continuar = False

valores = separar(cantArboles)

print(f'{len(valores[0])} ciudades plantaron mas de 100 arboles')