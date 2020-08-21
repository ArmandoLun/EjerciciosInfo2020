biologos = {}
continuar=True
while(continuar):
    nombre = input("Ingrese nombre: ")
    email = input("Ingrese email: ")
    if(not(nombre in biologos)):
        biologos[nombre]= email
    else:
        print('El nombre indicado ya está registrado.')
        print('Por favor, intente con otro nombre.')
        continue
    preg= input("Desea continuar? (s/n)")
    if(preg=='n'):
        continuar=False

print(biologos)