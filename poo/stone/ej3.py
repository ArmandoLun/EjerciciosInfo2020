class Triangulo:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def mostrarMayor(self):
        if (self.l1 >= self.l2 and self.l1 >= self.l3):
            print('Lado de tamanio mayor:', l1)
        elif (self.l2 >= self.l1 and self.l2 >= self.l3):
            print('Lado de tamanio mayor:', l2)
        else:
            print('Lado de tamanio mayor:', l3)

    def mostrarTipo(self):
        if (self.l1 == self.l2 and self.l2 == self.l3):
            print('Tipo: Equilatero')
        elif (self.l1 != self.l2 and self.l1 != self.l3):
            print('Tipo: Escaleno')
        else :
            print('Tipo: Isosceles')
        


l1 = int(input('Ingrese lado 1: '))
l2 = int(input('Ingrese lado 2: '))
l3 = int(input('Ingrese lado 3: '))

mi_trian = Triangulo(l1, l2, l3)
mi_trian.mostrarTipo()
mi_trian.mostrarMayor()