def relacion(a,b):
    if(a['toneladas']>b['toneladas']):
        return a['nombre']
    elif (b['toneladas']>a['toneladas']):
        return b['nombre']
    else:
        c = a['nombre'] + ' y ' + b['nombre']
        return c

ciudades = []

for i in range(2):
    nombre = input('Ingrese nombre de la ciudad: ')
    toneladas = float(input('Ingrese toneladas recicladas: '))
    ciudad = {
        'nombre' : nombre,
        'toneladas' : toneladas
    }
    ciudades.append(ciudad)

print(relacion(ciudades[0], ciudades[1]))