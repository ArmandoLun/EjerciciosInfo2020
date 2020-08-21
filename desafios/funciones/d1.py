def tiempoDegradacion(elem):
    if (elem == 'Bolsa de plástico'):
        print('Se degrada en 150 años')
    elif (elem == 'Botella PET'):
        print('Se degrada en 1000 años')
    elif(elem=='Envase tetrabrik'):
        print("Se degrada en 30 años")
    elif(elem == 'Chicle'):
        print("Se degrada en 5 años")
    else:
        print('Elemento invalido')

elemento = input("Ingrese el elemento: ")
tiempoDegradacion(elemento)
