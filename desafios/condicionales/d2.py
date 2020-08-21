# Desafio 2 - Contaminacion en peces

print("Indique tamaño del pez:")
print("\n1: Tamaño normal\n2: Tamaño por debajo de lo normal")
print("3: Tamaño por encima de lo normal\n4: Tamaño sobredimensionado")

tamaño = int(input())

if(tamaño==1):
    print("\nPez en buenas condiciones")
elif(tamaño==2):
    print("\nPez con problemas de nutrición")
elif(tamaño==3):
    print("\nPez con síntomas de organismo contaminado")
elif(tamaño==4):
    print("\nPez contaminado")