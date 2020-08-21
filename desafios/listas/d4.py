especies = []
continuar = True

while(continuar):
    nombre = input("Ingrese nombre de la especie: ")
    especies.append(nombre)

    preg=input("Cargar mas especies? (s/n)")
    if(preg=='n'):
        continuar=False

especies = tuple(especies)

p = int(input(f"Indique pos. inicial (0 - {len(especies)-1}): "))
n = int(input(f"Cuantos desea saludar? (1 - {len(especies)}): "))

for i in range(p, n):
    print(especies[i])