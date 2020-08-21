# Desafio 4 - Tablero
celda=True
for i in range(6):
    for j in range(8):
        if celda:
            print("\033[1;32;40m verde", end=" ")
        else:
            print("\033[1;37;40m blanco", end=" ")
        celda=not(celda)
    celda=not(celda)
    print("\n")
    